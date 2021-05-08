from global_constants import *
import pygame
from time import sleep

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.size = list(map(lambda x: x * SCALE, PLAYERSIZE))

        self.image = pygame.image.load('./sprites/GameJam Miel.png')
        self.image = pygame.transform.scale(self.image, self.size)


        self.rect = self.image.get_rect()


    def _move(self, x, y):

        self.rect.x += x * self.size[0]
        self.rect.y += y * self.size[1]

        # todo deuren enzo
        tile = TILESIZE * SCALE
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > (HEIGHT * SCALE - tile):
            self.rect.y = (HEIGHT * SCALE - tile)

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > (WIDTH * SCALE - tile):
            self.rect.x = (WIDTH * SCALE - tile)

        sleep(MOVEDELAY)

    def move_up(self):
        # 1 tile naar boven
        self._move(0, -1)

    def move_down(self):
        self._move(0, 1)

    def move_right(self):
        self._move(1, 0)

    def move_left(self):
        self._move(-1, 0)