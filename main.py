from Player import Player
import pygame
from World import World
from global_constants import *
from Room import WALL

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
    if pygame.sprite.collide_mask(player, WALL):
        print("collision!")

def input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.move_up()
    elif keys[pygame.K_s]:
        player.move_down()
    if keys[pygame.K_a]:
        player.move_left()
    elif keys[pygame.K_d]:
        player.move_right()

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
        update()
        draw()
    pygame.quit()


if __name__ == "__main__":
    main()
