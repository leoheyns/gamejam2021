from Room import Room
from global_constants import * 

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


class World:

    rooms = []
    current_coords = (0,0)

    def __init__(self):
        for x in range(WORLD_DIM[0]):
            self.rooms.append([])
            for y in range(WORLD_DIM[1]):
                self.rooms[x].append(Room([True,True,True,True]))


    def draw(self, WIN):
        print(self.current_coords)
        self.rooms[self.current_coords[0]][self.current_coords[1]].draw(WIN)
    
    def update(self):
        pass

    def move(self,direction):
        self.current_coords = attempt_move(self.current_coords, direction)
