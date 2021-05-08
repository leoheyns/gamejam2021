from Room import Room
from global_constants import * 
import random

def attempt_move(coords, direction):
    if direction == 1:
        if coords[1] > 0:
            return coords[0],coords[1]-1
    elif direction == 2:
        if coords[0] < WORLD_DIM[0] - 1:
            return coords[0] + 1,coords[1]
    elif direction == 3:
        if coords[1] < WORLD_DIM[1] - 1:
            return coords[0],coords[1] + 1
    elif direction == 4:
        if coords[0] > 0:
            return coords[0] - 1,coords[1]
    return coords

def room_at_dir(coords, direction):
    if direction == 0:
            return coords[0],coords[1]-1
    elif direction == 1:
            return coords[0] + 1,coords[1]
    elif direction == 2:
            return coords[0],coords[1] + 1
    elif direction == 3:
            return coords[0] - 1,coords[1]

def surrounding_coords(coord):
    return {(coord[0], coord[1] + 1), (coord[0] + 1, coord[1]), (coord[0], coord[1] - 1), (coord[0] -1, coord[1])}

def door_pair(pos1, pos2):
    if pos1[0] > pos2[0]:
        return 3,1
    if pos1[0] < pos2[0]:
        return 1,3
    if pos1[1] > pos2[1]:
        return 0,2
    if pos1[1] < pos2[1]:
        return 2,0

class World:

    rooms = []
    current_coords = (0,0)

    room_dict = {}

    def __init__(self):
        self.room_dict[(0,0)] = Room()

        for i in range(ROOM_COUNT - 1):
            while True:
                frontier_room = random.choice(list(self.room_dict.keys()))
                expandable_rooms = surrounding_coords(frontier_room) - self.room_dict.keys()
                if len(expandable_rooms) == 0:
                    continue

                expand_room = random.choice(list(expandable_rooms))
                self.room_dict[expand_room] = Room()

                #open doors between old and new room
                f_door, e_door = door_pair(frontier_room, expand_room)
                self.room_dict[frontier_room].doors[f_door] = True

                self.room_dict[expand_room].doors[e_door] = True


                break

        for room in self.room_dict.values():
            room.generate()

        # for x in range(WORLD_DIM[0]):
        #     self.rooms.append([])
        #     for y in range(WORLD_DIM[1]):
        #         self.rooms[x].append(Room([True,True,True,True]))


    def draw(self, WIN):
        self.room_dict[self.current_coords].draw(WIN)
        # self.rooms[self.current_coords[0]][self.current_coords[1]].draw(WIN)
    
    def update(self):
        pass

    def move(self,direction):
        target_room = room_at_dir(self.current_coords, direction)
        if self.room_dict[self.current_coords].doors[direction]:
            self.current_coords = target_room
        # if target_room in self.room_dict.keys():
        #     self.current_coords = target_room