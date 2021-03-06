import pygame as pygame

import SoundWave
from Room import Room, ROOMHEIGHT, ROOMWIDTH, FREE_SPACES
from global_constants import *
import random
import pygame
import math

pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 15)
DOOR_PROB = 0.3

pygame.mixer.init()

items = {pygame.image.load(resource_path('sprites/GameJam Bongos.png')): pygame.mixer.Sound(resource_path('sounds/Bongo.wav')),
         pygame.image.load(resource_path('sprites/GameJam Guitar.png')): pygame.mixer.Sound(resource_path('sounds/Guitar.wav')),
         pygame.image.load(resource_path('sprites/GameJam keyboard.png')): pygame.mixer.Sound(resource_path('sounds/Keyboard.wav')),
         pygame.image.load(resource_path('sprites/GameJam Trumpet.png')): pygame.mixer.Sound(resource_path('sounds/Trumpet.wav'))}


def attempt_move(coords, direction):
    if direction == 1:
        if coords[1] > 0:
            return coords[0], coords[1] - 1
    elif direction == 2:
        if coords[0] < WORLD_DIM[0] - 1:
            return coords[0] + 1, coords[1]
    elif direction == 3:
        if coords[1] < WORLD_DIM[1] - 1:
            return coords[0], coords[1] + 1
    elif direction == 4:
        if coords[0] > 0:
            return coords[0] - 1, coords[1]
    return coords


def room_at_dir(coords, direction):
    if direction == 0:
        return coords[0], coords[1] - 1
    elif direction == 1:
        return coords[0] + 1, coords[1]
    elif direction == 2:
        return coords[0], coords[1] + 1
    elif direction == 3:
        return coords[0] - 1, coords[1]


def surrounding_coords(coord):
    return {(coord[0], coord[1] + 1), (coord[0] + 1, coord[1]), (coord[0], coord[1] - 1), (coord[0] - 1, coord[1])}


def door_pair(pos1, pos2):
    if pos1[0] > pos2[0]:
        return 3, 1
    if pos1[0] < pos2[0]:
        return 1, 3
    if pos1[1] > pos2[1]:
        return 0, 2
    if pos1[1] < pos2[1]:
        return 2, 0


class World:
    current_coords = (0, 0)

    room_dict = {}
    items_enabled = {False, False, False, False}

    def __init__(self):
        self.room_dict[(0, 0)] = Room(gen_enemies=False)
        SoundWave.calculate_circles(16)

        for i in range(ROOM_COUNT - 1):
            while True:
                frontier_room = random.choice(list(self.room_dict.keys()))
                expandable_rooms = surrounding_coords(frontier_room) - self.room_dict.keys()
                if len(expandable_rooms) == 0:
                    continue

                expand_room = random.choice(list(expandable_rooms))

                if ROOM_COUNT - i - 2 < len(items.keys()):
                    print(list(items.keys())[ROOM_COUNT - 2 - i], expand_room)
                    self.room_dict[expand_room] = Room(item=list(items.keys())[ROOM_COUNT - i - 2])
                else:
                    self.room_dict[expand_room] = Room()

                # open doors between old and new room
                f_door, e_door = door_pair(frontier_room, expand_room)
                self.room_dict[frontier_room].doors[f_door] = True

                self.room_dict[expand_room].doors[e_door] = True

                break

        # open more doors
        for room in self.room_dict.keys():
            neighbours = surrounding_coords(room).intersection(self.room_dict.keys())
            for neighbour in neighbours:
                # adjusted probability because each door gets 2 chances
                adjusted_prob = 1 - math.sqrt(1 - DOOR_PROB)
                if random.random() < adjusted_prob:
                    r_door, n_door = door_pair(room, neighbour)
                    self.room_dict[room].doors[r_door] = True
                    self.room_dict[neighbour].doors[n_door] = True

        for room in self.room_dict.values():
            room.generate()

        self.room_items = {}

        for room in self.room_dict.values():
            if room.item is not None:
                spaces = set()
                for x in range(ROOMWIDTH):
                    for y in range(ROOMHEIGHT):
                        if FREE_SPACES[y][x] == "_":
                            spaces.add((x * TILESIZE, y * TILESIZE))

                self.room_items[room] = (room.item, random.sample(spaces, 1)[0])

        # for x in range(WORLD_DIM[0]):
        #     self.rooms.append([])
        #     for y in range(WORLD_DIM[1]):
        #         self.rooms[x].append(Room([True,True,True,True]))

    def draw(self, WIN):
        room = self.room_dict[self.current_coords]

        room.draw(WIN)

        if room in self.room_items.keys():
            if not room.item_found:
                WIN.blit(self.room_items[room][0], self.room_items[room][1])

        textsurface = font.render(str(self.current_coords), False, (255, 255, 255))
        WIN.blit(textsurface, (0, 0))
        # self.rooms[self.current_coords[0]][self.current_coords[1]].draw(WIN)

    def update(self):
        self.get_current_room().update()

    def get_current_room(self) -> Room:
        return self.room_dict[self.current_coords]

    def move(self, direction):
        target_room = room_at_dir(self.current_coords, direction)
        if self.room_dict[self.current_coords].doors[direction]:
            self.current_coords = target_room
        # if target_room in self.room_dict.keys():
        #     self.current_coords = target_room

    def reset(self):
        self.current_coords = (0, 0)

        for room in self.room_dict.values():
            room.item_found = False
