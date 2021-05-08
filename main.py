from Player import Player
import pygame

from SoundWave import SoundWave
from World import World
from global_constants import *
from Room import WALL
import copy

FPS = 60
SCALE = 3
WIDTH, HEIGHT = ROOM_DIM[0] * TILESIZE, ROOM_DIM[1] * TILESIZE

WIN = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
pygame.display.set_caption("wie dit leest trekt een ad")

world = World()

sprite_group = pygame.sprite.Group()
player = Player()
sprite_group.add(player)

waves = []
SOUNDWAVE = pygame.USEREVENT+1


def draw():
    temp_win = pygame.Surface((WIDTH, HEIGHT))
    world.draw(temp_win)
    temp_win = pygame.transform.scale(temp_win, (WIDTH * 3, HEIGHT * 3))
    WIN.blit(temp_win, (0, 0))

    # draw all sprites
    sprite_group.draw(WIN)

    for wave in waves:
        wave.draw(WIN, world.get_current_room())
        if wave.remove:
            waves.remove(wave)

    pygame.display.update()


def update():
    # pygame.sprite.spritecollide(player, )
    pass

def input():
    keys = pygame.key.get_pressed()
    # has_wall = world.get_current_room().has_wall(*player.current_pos)
    room = world.get_current_room()
    pos = copy.deepcopy(player.current_pos)
    # print(pos)
    if keys[pygame.K_w]:
        pos[1] -= 1
        player.move_up(room.has_wall(*pos))
    elif keys[pygame.K_s]:
        pos[1] += 1
        player.move_down(room.has_wall(*pos))
    elif keys[pygame.K_a]:
        pos[0] -= 1
        player.move_left(room.has_wall(*pos))
    elif keys[pygame.K_d]:
        pos[0] += 1
        player.move_right(room.has_wall(*pos))

def keydown(event):
    if event.key == pygame.K_UP:
        world.move(1)
    if event.key == pygame.K_RIGHT:
        world.move(2)
    if event.key == pygame.K_DOWN:
        world.move(3)
    if event.key == pygame.K_LEFT:
        world.move(4)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    pygame.time.set_timer(SOUNDWAVE, 3000)
    # waves.append(SoundWave(round(500 + 32 // 2), round(500 + 32 // 2), 16, (255, 0, 0), SCALE))

    while run:
        clock.tick(FPS)

        for wave in waves:
            if wave.radius + wave.vel < WIN.get_width():
                if wave.count == 0:
                    wave.radius += wave.vel
                    wave.count = 25
                else:
                    wave.count -= 1
            else:
                waves.remove(wave)

        for event in pygame.event.get():
            if event.type == SOUNDWAVE:
                x = 500
                y = 500
                waves.append(SoundWave(x, y, 16, (255, 0, 0), SCALE))
                # TODO change x, y to location of enemy
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                keydown(event)
        input()

        draw()
        update()
    pygame.quit()


if __name__ == "__main__":
    main()
