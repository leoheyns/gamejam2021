import pygame
from global_constants import *
from SoundWave import SoundWave

asset = resource_path('sprites/GameJam minion enemy.png')
ENEMY = pygame.image.load(asset)
ENEMY = pygame.transform.scale(ENEMY, (TILESIZE, TILESIZE))

INTERVAL = 300


class Enemy:
    def __init__(self, x, y, room, start_cooldown = 0):
        self.x = x
        self.y = y
        self.cooldown = start_cooldown
        self.start_cooldown = start_cooldown
        self.waves = []
        self.room = room

    def draw(self, WIN, blits):
        blits.append((ENEMY, (self.x, self.y)))

        before = len(blits)
        for wave in self.waves:
            wave.draw(WIN, self.room, blits)
            if wave.remove:
                self.waves.remove(wave)
        after = len(blits)

    def update(self):
        print(self.cooldown)
        if self.cooldown <= 0:
            #todo spawn soundwave
            self.waves.append(SoundWave(round(self.x + 32 // 2), round(self.y + 32 // 2), 16, (255, 0, 0, 75)))
            self.cooldown = INTERVAL
        self.cooldown -= 1   

        for wave in self.waves:
            if wave.radius + wave.vel < WIDTH:
                if wave.count == 0:
                    wave.radius += wave.vel
                    wave.count = 25
                else:
                    wave.count -= 1
            else:
                self.waves.remove(wave)

    def reset(self):
        self.waves = []
        self.cooldown = self.start_cooldown
