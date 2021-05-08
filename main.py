from Player import Player
import pygame
from World import World
from global_constants import *
from Room import WALL
import copy

FPS = 60

WIN = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
pygame.display.set_caption("wie dit leest trekt een ad")

world = World()

sprite_group = pygame.sprite.Group()
player = Player()
sprite_group.add(player)

def draw():
    temp_win = pygame.Surface((WIDTH, HEIGHT))
    world.draw(temp_win)
    temp_win = pygame.transform.scale(temp_win, (WIDTH * 3, HEIGHT * 3))
    WIN.blit(temp_win, (0,0))

    # draw all sprites
    sprite_group.draw(WIN)

    pygame.display.update()


def update():
    # pygame.sprite.spritecollide(player, )
    pass

def input():
    keys = pygame.key.get_pressed()
    room = world.get_current_room()
    pos = copy.deepcopy(player.current_pos)
    if keys[pygame.K_w]:
        print(room.is_door(*pos))
        if room.is_door(*pos):
            world.move(1)
            player.move_door(1)
            pass
        pos[1] -= 1
        player.move_up(room.has_wall(*pos))
    elif keys[pygame.K_s]:
        print(room.is_door(*pos))
        # if room.is_door(*pos):
        #     print(f'door at {pos}')
        #     world.move(3)
        #     player.move_door(3)
        #     pass
        pos[1] += 1
        player.move_down(room.has_wall(*pos))
    elif keys[pygame.K_a]:
        # if room.is_door(*pos):
        #     world.move(4)
        #     pass
        pos[0] -= 1
        player.move_left(room.has_wall(*pos))
    elif keys[pygame.K_d]:
        # if room.is_door(*pos):
        #     world.move(2)
        #     pass
        pos[0] += 1
        player.move_right(room.has_wall(*pos))

def keydown(event):
    if event.key == pygame.K_UP:
        world.move(0)
    if event.key == pygame.K_RIGHT:
        world.move(1)
    if event.key == pygame.K_DOWN:
        world.move(2)
    if event.key == pygame.K_LEFT:
        world.move(3)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
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
