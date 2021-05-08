from global_constants import *
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, scale):
        super().__init__()

        self.size = list(map(lambda x: x * scale, PLAYERSIZE))

        self.image = pygame.Surface(self.size)
        self.image.fill((0, 0, 0)) # tijdelijke kleur
        self.image.set_colorkey((0, 0, 0))

        pygame.draw.rect(self.image, (0, 255, 0), [0, 0, self.size[0], self.size[1]])

        self.rect = self.image.get_rect()


    def _move(self, x, y):
        self.rect.x += x * (self.size[0]/2)
        self.rect.y += y * (self.size[1]/2)

        # niet van het scherm af schieten
        # todo deuren enzo
        if self.rect.y < 0:
            self.rect.y = 0
        # todo niet van onderkant van scherm af
        # of collision detection ofzo

    def move_up(self):
        # 1 tile naar boven
        self._move(0, -1)

    def move_down(self):
        self._move(0, 1)

    def move_right(self):
        self._move(1, 0)

    def move_left(self):
        self._move(-1, 0)