import numpy as np
import pygame
from global_constants import *

WIDTH = ROOM_DIM[0]
HEIGTH = ROOM_DIM[1]

TILE = pygame.Rect(0, 0, SPRITESIZE, SPRITESIZE)

GROUND = pygame.image.load('sprites/GameJam floor.png')
GROUND = pygame.transform.scale(GROUND, (TILESIZE, TILESIZE))

MOSSY_GROUND = pygame.image.load('sprites/GameJam floor mossy.png')
MOSSY_GROUND = pygame.transform.scale(MOSSY_GROUND, (TILESIZE, TILESIZE))

WALL = pygame.image.load('sprites/GameJam wall.png')
WALL = pygame.transform.scale(WALL, (TILESIZE, TILESIZE))


DISTRIBUTION = [2,5,1]
TILES = [WALL,GROUND, MOSSY_GROUND]


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

                # ontzichtbare muur voor collision detection
                if TILES[self.background[i,j]] == WALL:
                    pygame.draw.rect(WALL, (0,0,0), [i * TILESIZE, j * TILESIZE, TILESIZE, TILESIZE])
                    
        WIN.blits(blits)
    
    def update(self):
        pass