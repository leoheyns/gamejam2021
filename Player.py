from global_constants import *
import pygame
from time import sleep

class Player(pygame.sprite.Sprite):

    current_pos = [4, 4]
    last_time   = 0
    tp_time     = 0

    def __init__(self):
        super().__init__()

        self.last_time = pygame.time.get_ticks()
        self.tp_time   = self.tp_time

        self.size = list(map(lambda x: x * SCALE, PLAYERSIZE))

        self.image = pygame.image.load('./sprites/GameJam Miel.png')
        self.image = pygame.transform.scale(self.image, self.size)

        self.rect = self.image.get_rect()

        self.rect.x = self.current_pos[0] * TILESIZE * SCALE
        self.rect.y = self.current_pos[1] * TILESIZE * SCALE


    def _move(self, x, y, world):
        time = pygame.time.get_ticks()

        if time < self.last_time + MOVEDELAY:
            return

        self.last_time = time

        if (self._can_move(self.current_pos[0] + x, self.current_pos[1] + y)):
            self.rect.x += x * self.size[0]
            self.rect.y += y * self.size[1]
            self.current_pos[0] = self.current_pos[0] + x
            self.current_pos[1] = self.current_pos[1] + y




    def _can_move(self, toX, toY):
        cur = self.current_pos

        if toX < 0 or toX >= ROOM_DIM[0]:
            return False
        elif toY < 0 or toY >= ROOM_DIM[1]:
            return False
        return True


    def _move_to(self, x, y):
        time = pygame.time.get_ticks()

        if time < self.tp_time + 500:
            print("cant teleport rn")
            return

        self.tp_time = time

        self.rect.x = x * self.size[0]
        self.rect.y = y * self.size[1]

        self.current_pos = [x, y]

    def move_up(self, wall, world):
        if not wall: self._move(0, -1, world)
        if world.get_current_room().is_door(*self.current_pos): 
            self.move_door(0)
            world.move(0)

    def move_down(self, wall, world):
        if not wall: self._move(0, 1, world)
        if world.get_current_room().is_door(*self.current_pos): 
            self.move_door(2)
            world.move(2)

    def move_right(self, wall, world):
        if not wall:
            self._move(1, 0, world)
        if world.get_current_room().is_door(*self.current_pos): 
            self.move_door(1)
            world.move(1)

    def move_left(self, wall, world):
        if not wall:
            self._move(-1, 0, world)
        if world.get_current_room().is_door(*self.current_pos):
            self.move_door(3)
            world.move(3)


    def move_door(self, direction):
        print("move_door")
        if direction == 0:
            self._move_to(4, 4)
            # self._move_to(self.current_pos[0], ROOM_DIM[1] - 1)
        elif direction == 1:
            self._move_to(4, 4)
            # self._move_to(1, self.current_pos[1])
        elif direction == 2:
            self._move_to(4, 4)
            # self._move_to(self.current_pos[0], 0)
        elif direction == 3:
            self._move_to(4, 4)
            # self._move_to(ROOM_DIM[0] - 1, 0)