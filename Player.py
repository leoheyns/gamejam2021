from global_constants import *
import pygame
from time import sleep

class Player(pygame.sprite.Sprite):

    current_pos = [4, 4]
    last_time = 0

    def __init__(self):
        super().__init__()

        self.last_time = pygame.time.get_ticks()

        self.size = list(map(lambda x: x * SCALE, PLAYERSIZE))

        self.image = pygame.image.load('./sprites/GameJam Miel.png')
        self.image = pygame.transform.scale(self.image, self.size)

        self.rect = self.image.get_rect()

        self.rect.x = self.current_pos[0] * TILESIZE * SCALE
        self.rect.y = self.current_pos[1] * TILESIZE * SCALE


    def _move(self, x, y):
        time = pygame.time.get_ticks()

        if time < self.last_time + MOVEDELAY:
            return

        self.last_time = time

        print(self.current_pos)
        self.rect.x += x * self.size[0]
        self.rect.y += y * self.size[1]

        tile = TILESIZE * SCALE
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y >= (HEIGHT * SCALE - tile):
            self.rect.y = (HEIGHT * SCALE - tile)
        else:
            self.current_pos[1] = self.current_pos[1] + y

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x >= (WIDTH * SCALE - tile):
            self.rect.x = (WIDTH * SCALE - tile)
        else:
            self.current_pos[0] = self.current_pos[0] + x


    def _move_to(self, x, y):
        self.rect.x = x * self.size[0]
        self.rect.y = y * self.size[1]

        self.current_pos = [x, y]

    def move_up(self, wall):
        # 1 tile naar boven
        if not wall: self._move(0, -1)

    def move_down(self, wall):
        if not wall: self._move(0, 1)

    def move_right(self, wall):
        if not wall: self._move(1, 0)

    def move_left(self, wall):
        if not wall: self._move(-1, 0)

    def move_door(self, direction):
        print("move_door")
        if direction == 1:
            self._move_to(4,4)
            pass
        elif direction == 2:
            pass
        elif direction == 3:
            self._move_to(4,4)
        elif direction == 4:
            pass