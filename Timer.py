import pygame
from global_constants import *

font = pygame.font.SysFont('Comic Sans MS', 15)

class Timer():
    running = None
    ticks = None
    startticks = None
    def __init__(self, ticks):
        self.running = False
        self.startticks = ticks
        self.ticks = ticks

    def draw(self, WIN):
        textsurface = font.render(f"{self.ticks // 60}.{self.ticks % 60}", False, (255,255,255))
        WIN.blit(textsurface, (TILESIZE * (ROOM_DIM[0] - 2),0))

    def update(self):
        self.ticks -= 1
        if self.ticks <= 0:
            pygame.event.post(pygame.event.Event(TIMER_ZERO))

    
    def start(self):
        self.running = True

    def reset(self):
        self.running = False
        self.ticks = self.startticks