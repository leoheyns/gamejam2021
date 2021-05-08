import numpy as np
import pygame
from global_constants import *

WIDTH = ROOM_DIM[0]
HEIGTH = ROOM_DIM[1]

TILE = pygame.Rect(0, 0, TILESIZE, TILESIZE)
GROUND = pygame.Surface((TILESIZE, TILESIZE))
BROWN = (155, 118, 83)
pygame.draw.rect(GROUND, BROWN, TILE)
# GROUND = pygame.transform.scale(GROUND, (TILESIZE, TILESIZE))

WALL = pygame.Surface((TILESIZE, TILESIZE))
GREY = (128, 128, 128)
pygame.draw.rect(WALL, GREY, TILE)
# WALL = pygame.transform.scale(WALL, (TILESIZE, TILESIZE))

DISTRIBUTION = [1,3]
TILES = [WALL,GROUND]


def is_middle_of(i, n):
    if n % 2 == 0:
        return i == n / 2 or i == (n / 2) - 1
    else:
        return i == (n // 2)

class Room:

    background = None

    def __init__(self, doors):
        rand_values = np.random.randint(0, sum(DISTRIBUTION), (WIDTH,HEIGTH))
        self.background = np.zeros_like(rand_values)
        for i in range(WIDTH):
            for j in range(HEIGTH):
                for k in range(len(DISTRIBUTION)):
                    if rand_values[i,j] < sum(DISTRIBUTION[:k + 1]):
                        self.background[i,j] = k
                        break
        

        #set walls all around
        for i in range(WIDTH):
            #set door
            if is_middle_of(i, WIDTH) & doors[0]:
                self.background[i,0] = 1
            #set wall
            else:
                self.background[i,0] = 0

            if is_middle_of(i, WIDTH) & doors[2]:
                self.background[i,HEIGTH-1] = 1
            else:
                self.background[i,HEIGTH-1] = 0
        
        for i in range(HEIGTH):
            #set door
            if is_middle_of(i, HEIGTH) & doors[3]:
                self.background[0, i] = 1
            #set wall
            else:
                self.background[0, i] = 0

            if is_middle_of(i, HEIGTH) & doors[1]:
                self.background[WIDTH-1, i] = 1
            else:
                self.background[WIDTH-1, i] = 0
        


    def draw(self, WIN):
        blits = []
        for i in range(WIDTH):
            for j in range(HEIGTH):
                blits.append((TILES[self.background[i,j]], (i * TILESIZE, j * TILESIZE)))

        WIN.blits(blits)
    
    def update(self):
        pass