import pygame
import sys
import os

TILESIZE   = 32
PLAYERSIZE = [32, 32]
SPRITESIZE = 32

ROOM_DIM  = (16,9)
WORLD_DIM = (5,5)

WIDTH, HEIGHT = ROOM_DIM[0] * TILESIZE, ROOM_DIM[1] * TILESIZE
SCALE = 3

MOVEDELAY = 110
ROOM_DIM = (16,9)
ROOM_COUNT = 25

TIMER_ZERO = pygame.USEREVENT + 1

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)