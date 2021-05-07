import numpy as np
import pygame

HEIGTH = 18
WIDTH = 32

TILESIZE = 32

TILE = pygame.Rect(0, 0, TILESIZE, TILESIZE)
GROUND = pygame.Surface((TILESIZE, TILESIZE))
BROWN = (155, 118, 83)
pygame.draw.rect(GROUND, BROWN, TILE)

WALL = pygame.Surface((TILESIZE, TILESIZE))
GREY = (128, 128, 128)
pygame.draw.rect(WALL, GREY, TILE)

class Room:

    background = None

    def __init__(self):
        self.background = np.random.randint(0, 10, (32,18))

    def draw(self, WIN):
        blits = []
        for i in range(WIDTH):
            for j in range(HEIGTH):
                if self.background[i,j] > 1:
                    blits.append((GROUND, (i * TILESIZE, j * TILESIZE)))
                else:
                    blits.append((WALL, (i * TILESIZE, j * TILESIZE)))
        WIN.blits(blits)
    
    def update(self):
        pass