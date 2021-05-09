import numpy as np
import pygame
from global_constants import *
import random
from Enemy import Enemy
from Player import Player

WIDTH = ROOM_DIM[0]
HEIGTH = ROOM_DIM[1]

TILE = pygame.Rect(0, 0, TILESIZE, TILESIZE)

GROUND = pygame.image.load('sprites/GameJam floor.png')
GROUND = pygame.transform.scale(GROUND, (TILESIZE, TILESIZE))

MOSSY_GROUND = pygame.image.load('sprites/GameJam floor mossy.png')
MOSSY_GROUND = pygame.transform.scale(MOSSY_GROUND, (TILESIZE, TILESIZE))

SAND_MOSSY_GROUND = pygame.image.load('sprites/sandstone_mossy.png')
SAND_MOSSY_GROUND = pygame.transform.scale(SAND_MOSSY_GROUND, (TILESIZE, TILESIZE))

SAND_GROUND = pygame.image.load('sprites/sandstone_ground.png')
SAND_GROUND = pygame.transform.scale(SAND_GROUND, (TILESIZE, TILESIZE))

WALL = pygame.image.load('sprites/GameJam wall.png')
WALL = pygame.transform.scale(WALL, (TILESIZE, TILESIZE))

ENEMY = pygame.image.load('sprites/GameJam minion enemy.png')
ENEMY = pygame.transform.scale(ENEMY, (TILESIZE, TILESIZE))

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

DISTRIBUTION = [4,15,5]
TILES = [WALL,GROUND, MOSSY_GROUND]


def is_middle_of(i, n):
    if n % 2 == 0:
        return i == n / 2 or i == (n / 2) - 1
    else:
        return i == (n // 2)


class Room:
    background = None
    enemies = None

    walls = pygame.sprite.Group()
    doors = []
    door_coords = []
    biome = None

    def __init__(self, gen_enemies = True):
        self.biome = random.choice([0,1])
        if self.biome == 0:
            self.TILES = [WALL, GROUND, MOSSY_GROUND]
        elif self.biome == 1:
            self.TILES = [WALL, SAND_GROUND, SAND_MOSSY_GROUND]

        self.doors = [False] * 4
        self.door_coords = [(-1,-1)] * 4
        self.gen_enemies = gen_enemies

    def generate(self):
        rand_values = np.random.randint(0, sum(DISTRIBUTION), (WIDTH, HEIGTH))
        self.background = np.zeros_like(rand_values)
        self.enemies = []
        for i in range(WIDTH):
            for j in range(HEIGTH):
                for k in range(len(DISTRIBUTION)):
                    if rand_values[i, j] < sum(DISTRIBUTION[:k + 1]):
                        self.background[i, j] = k
                        break
        for x in range(WIDTH):
            for y in range(HEIGTH):
                if FREE_SPACES[y][x] == "_":
                    # 1 is ground
                    self.background[x, y] = 1

        # set walls all around
        for i in range(WIDTH):
            # set door
            if is_middle_of(i, WIDTH) & self.doors[0]:
                self.background[i, 0] = 1
                self.door_coords[0] = (i, 0)
            # set wall
            else:
                self.background[i, 0] = 0

            if is_middle_of(i, WIDTH) & self.doors[2]:
                self.background[i, HEIGTH - 1] = 1
                self.door_coords[2] = (i, HEIGTH - 1)
            else:
                self.background[i, HEIGTH - 1] = 0

        for i in range(HEIGTH):
            # set door
            if is_middle_of(i, HEIGTH) & self.doors[3]:
                self.background[0, i] = 1
                self.door_coords[3] = (0, i)
            # set wall
            else:
                self.background[0, i] = 0

            if is_middle_of(i, HEIGTH) & self.doors[1]:
                self.background[WIDTH - 1, i] = 1
                self.door_coords[1] = (WIDTH - 1, i)
            else:
                self.background[WIDTH-1, i] = 0
            
        grounds = []
        for i in range(WIDTH):
            for j in range(HEIGTH):
                if (self.background[i,j] == 1 or self.background[i,j] == 2) & (FREE_SPACES[j][i] == "#"):
                    grounds.append((i,j))
        
        if self.gen_enemies:
            e_count = random.choices([1,2,3], weights=[10,60,30], k=1)[0]
            e_poss = random.sample(grounds, e_count)
            for pos in e_poss:
                self.enemies.append(Enemy(pos[0] * TILESIZE, pos[1] * TILESIZE, self))

        
    def has_wall(self, x, y):
        try:
            return self.background[x, y] == 0
        except IndexError:
            return False

    def has_wall(self, x, y):
        try:
            return self.background[x, y] == 0
        except IndexError:
            return True

    def is_miel(self, x, y):
        print("x,y:", x, y)
        print("player x, y:", Player.current_pos[0], Player.current_pos[1])
        return x == Player.current_pos[0] and y == Player.current_pos[1]


    def is_door(self, x, y, direction):
        return (x == 0 and direction == "left") \
               or (x == ROOM_DIM[0] - 1 and direction == "right") \
               or y == 0 and direction == "up"\
               or y == ROOM_DIM[1] - 1 and direction == "down"

    def draw(self, WIN):
        blits = []
        for i in range(WIDTH):
            for j in range(HEIGTH):
                blits.append((self.TILES[self.background[i,j]], (i * TILESIZE, j * TILESIZE)))
        
        for e in self.enemies:
            e.draw(WIN, blits)

        WIN.blits(blits)

    def update(self):
        for e in self.enemies:
            e.update()
