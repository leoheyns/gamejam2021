import pygame
import math

from global_constants import *


def round16(num):
    return int(16 * round(float(num)/16))


circles = {}


def calculate_circles(radius, scale):
    # Calculates all circles at the start, which can be used later
    for width in range(2, WIDTH):
        offs = set()

        for i in range(128, 0, -1):
            # if 8 > i > width * radius // scale:
            #     break

            for j in range(8):
                offs.add((round16(width * radius * math.cos(math.pi / (i / 32) + j * (math.pi / 2))),
                          round16(width * radius * math.sin(math.pi / (i / 32) + j * (math.pi / 2)))))

        circles[width] = offs


class SoundWave (object):
    previous_pixels = set()
    remove = False
    vel = 16
    count = 25
    pixel_coords = set()

    def __init__(self, x, y, radius, color, scale):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.scale = scale

        if len(circles) == 0:
            calculate_circles(16, 3)

    def draw_previous(self, window):
        for pixel in self.previous_pixels:
            pygame.draw.rect(window, (0, 0, 0),
                             (pixel[0]*self.scale, pixel[1]*self.scale, 16*self.scale, 16*self.scale))

    def draw(self, window, room):
        if self.radius//16 < 2:  # Do not draw if the radius is too small, so it starts outside the enemy
            return

        if self.count != 0:  # Do not recalculate all lines every frame
            self.draw_previous(window)
            return

        # Variables that store the tile of the center
        selfx = round16(self.x)//(self.scale * TILESIZE)
        selfy = round16(self.y)//(self.scale * TILESIZE)

        for pixel in circles[self.radius//16]:
            draw = True

            for i in range(1, 17):  # Do not draw if passing a wall
                if room.has_wall(math.floor(selfx*TILESIZE + pixel[0]*i/16)//32,
                                 math.floor(selfy*TILESIZE + pixel[1]*i/16)//32):
                    draw = False
                    break

            if draw:
                self.pixel_coords.add((selfx * TILESIZE + pixel[0], selfy * TILESIZE + pixel[1]))

        if len(self.pixel_coords) == 0:  # All pixels have been blocked by walls, so remove the wave
            self.remove = True

        for pixel in self.pixel_coords:
            if 0 <= pixel[0] <= ROOM_DIM[0]*TILESIZE and 0 <= pixel[1] <= ROOM_DIM[1]*TILESIZE:
                pygame.draw.rect(window, (0, 0, 0),
                                 (pixel[0]*self.scale, pixel[1]*self.scale, 16*self.scale, 16*self.scale))

        self.previous_pixels = self.pixel_coords.copy()
        self.pixel_coords.clear()
