from global_constants import *
import pygame


class Player(pygame.sprite.Sprite):
    current_pos = [7, 6]
    last_time = 0
    tp_time = 0

    def __init__(self, world):
        super().__init__()

        self.last_time = pygame.time.get_ticks()
        self.tp_time = self.tp_time

        self.world = world

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

        if self._can_move(self.current_pos[0] + x, self.current_pos[1] + y):
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

    def _move_to(self, x, y, dir):
        time = pygame.time.get_ticks()

        if time < self.tp_time + 300:
            return

        self.tp_time = time

        self.rect.x = x * self.size[0]
        self.rect.y = y * self.size[1]

        self.current_pos = [x, y]

        self.world.move(dir)

    def move_up(self, wall, world):
        if not wall: self._move(0, -1, world)
        if world.get_current_room().is_door(*self.current_pos, "up"):
            self.move_door(0)
            # world.move(0)

    def move_down(self, wall, world):
        if not wall: self._move(0, 1, world)
        if world.get_current_room().is_door(*self.current_pos, "down"):
            self.move_door(2)
            # world.move(2)

    def move_right(self, wall, world):
        if not wall: self._move(1, 0, world)
        if world.get_current_room().is_door(*self.current_pos, "right"):
            self.move_door(1)
            # world.move(1)

    def move_left(self, wall, world):
        if not wall: self._move(-1, 0, world)
        if world.get_current_room().is_door(*self.current_pos, "left"):
            self.move_door(3)
            # world.move(3)

    def move_door(self, direction):
        if direction == 0:
            self._move_to(self.current_pos[0], 8, direction)
        elif direction == 1:
            self._move_to(0, self.current_pos[1], direction)
        elif direction == 2:
            self._move_to(self.current_pos[0], 0, direction)
        elif direction == 3:
            self._move_to((ROOM_DIM[0] - 1), self.current_pos[1], direction)

    def reset(self):
        self.current_pos[0] = 7
        self.current_pos[1] = 6
        self.rect.x = self.current_pos[0] * TILESIZE * SCALE
        self.rect.y = self.current_pos[1] * TILESIZE * SCALE