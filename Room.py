import numpy as np
import pygame
from global_constants import *

WIDTH = ROOM_DIM[0]
HEIGTH = ROOM_DIM[1]

TILE = pygame.Rect(0, 0, TILESIZE, TILESIZE)

GROUND = pygame.image.load('sprites/GameJam floor.png')
GROUND = pygame.transform.scale(GROUND, (TILESIZE, TILESIZE))

MOSSY_GROUND = pygame.image.load('sprites/GameJam floor mossy.png')
MOSSY_GROUND = pygame.transform.scale(MOSSY_GROUND, (TILESIZE, TILESIZE))

WALL = pygame.image.load('sprites/GameJam wall.png')
WALL = pygame.transform.scale(WALL, (TILESIZE, TILESIZE))


FREE_SPACES = [
    "#######DD#######",
    "########_#######",
    "########____####",
    "###########____#",
    "D___#######_##_D",
    "###___#####_####",
    "#####_______####",
    "########_#######",
    "#######DD#######",
    ]

DISTRIBUTION = [2,5,1]
TILES = [WALL,GROUND, MOSSY_GROUND]


def is_middle_of(i, n):
    if n % 2 == 0:
        return i == n / 2 or i == (n / 2) - 1
    else:
        return i == (n // 2)

class Room:

    background = None

    walls = pygame.sprite.Group()
    doors = []
    door_coords = []

    def __init__(self):
        self.doors = [False] * 4
        self.door_coords = [(-1,-1)] * 4
        pass
        
    def generate(self):
        rand_values = np.random.randint(0, sum(DISTRIBUTION), (WIDTH,HEIGTH))
        self.background = np.zeros_like(rand_values)
        for i in range(WIDTH):
            for j in range(HEIGTH):
                for k in range(len(DISTRIBUTION)):
                    if rand_values[i,j] < sum(DISTRIBUTION[:k + 1]):
                        self.background[i,j] = k
                        break
        for x in range(WIDTH):
            for y in range(HEIGTH):
                if FREE_SPACES[y][x] == "_":
                    #1 is ground
                    self.background[x,y] = 1

        #set walls all around
        for i in range(WIDTH):
            #set door
            if is_middle_of(i, WIDTH) & self.doors[0]:
                self.background[i,0] = 1
                self.door_coords[0] = (i, 0)
            #set wall
            else:
                self.background[i,0] = 0

            if is_middle_of(i, WIDTH) & self.doors[2]:
                self.background[i,HEIGTH-1] = 1
                self.door_coords[2] = (i, HEIGTH-1)
            else:
                self.background[i,HEIGTH-1] = 0
        
        for i in range(HEIGTH):
            #set door
            if is_middle_of(i, HEIGTH) & self.doors[3]:
                self.background[0, i] = 1
                self.door_coords[3] = (0, i)
            #set wall
            else:
                self.background[0, i] = 0

            if is_middle_of(i, HEIGTH) & self.doors[1]:
                self.background[WIDTH-1, i] = 1
                self.door_coords[1] = (WIDTH-1, i)
            else:
                self.background[WIDTH-1, i] = 0
        
    def has_wall(self, x, y):
        try:
            return self.background[x, y] == 0
        except IndexError:
            return False

    def is_door(self, x, y):
        return x == 0 or x == ROOM_DIM[0] - 1 or y == 0 or y == ROOM_DIM[1] - 1

    def draw(self, WIN):
        blits = []
        for i in range(WIDTH):
            for j in range(HEIGTH):
                blits.append((TILES[self.background[i,j]], (i * TILESIZE, j * TILESIZE)))

        WIN.blits(blits)

    def update(self):
        pass