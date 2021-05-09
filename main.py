from Player import Player
import pygame

from SoundWave import calculate_circles, SoundWave
from World import World
from Timer import Timer
from global_constants import *
from Room import WALL
import copy


FPS = 60

WIN = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
pygame.display.set_caption("wie dit leest trekt een ad")

world = World()
timer = Timer(FPS * 60)

sprite_group = pygame.sprite.Group()
player = Player()
sprite_group.add(player)

waves = []
SOUNDWAVE = pygame.USEREVENT+2


def draw():
    temp_win = pygame.Surface((WIDTH, HEIGHT))
    world.draw(temp_win)
    timer.draw(temp_win)
    temp_win = pygame.transform.scale(temp_win, (WIDTH * 3, HEIGHT * 3))
    WIN.blit(temp_win, (0, 0))

    # draw all sprites
    sprite_group.draw(WIN)



    pygame.display.update()


def update():
    # pygame.sprite.spritecollide(player, )
    timer.update()
    world.update()

def reset():
    timer.reset()
    world.reset()
    timer.start()

def input():
    keys = pygame.key.get_pressed()
    room = world.get_current_room()
    pos = copy.deepcopy(player.current_pos)

    if keys[pygame.K_w]:
        pos[1] -=1
        player.move_up(room.has_wall(*pos), world)
    elif keys[pygame.K_s]:
        pos[1] += 1
        player.move_down(room.has_wall(*pos), world)
    elif keys[pygame.K_a]:
        pos[0] -= 1
        player.move_left(room.has_wall(*pos), world)
    elif keys[pygame.K_d]:
        pos[0] += 1
        player.move_right(room.has_wall(*pos), world)


def keydown(event):
    if event.key == pygame.K_UP:
        world.move(0)
    if event.key == pygame.K_RIGHT:
        world.move(1)
    if event.key == pygame.K_DOWN:
        world.move(2)
    if event.key == pygame.K_LEFT:
        world.move(3)
    if event.key == pygame.K_ESCAPE:
        pause()

def intro():
    titlescreen = pygame.image.load('sprites/GameJam Titel Engels.png')
    titlescreen = pygame.transform.scale(titlescreen, (WIDTH * 3, HEIGHT * 3))
    clock = pygame.time.Clock()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if 520 <= y <= 670:
                    if 110 <= x <= 515:
                        return
                    if 1015 <= x <= 1430:
                        pygame.quit()
                        quit()

        WIN.blit(titlescreen, (0, 0))
        pygame.display.update()
        clock.tick(FPS)


def pause():
    menuscreen = pygame.image.load('sprites/GameJam menu.png')
    menuscreen = pygame.transform.scale(menuscreen, (WIDTH * 3, HEIGHT * 3))
    clock = pygame.time.Clock()
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if 444 <= x <= 1092:
                    if 67 <= y <= 216:
                        return
                if 562 <= x <= 973:
                    if 260 <= y <= 407:
                        main()
                if 468 <= x <= 1068:
                    if 450 <= y <= 597:
                        game()
                if 602 <= x <= 934:
                    if 644 <= y <= 793:
                        pygame.quit()
                        quit()
        WIN.blit(menuscreen, (0, 0))
        pygame.display.update()
        clock.tick(FPS)


def game():

    clock = pygame.time.Clock()
    run = True
    timer.start()
    pygame.time.set_timer(SOUNDWAVE, 3000)
    # waves.append(SoundWave(round(500 + 32 // 2), round(500 + 32 // 2), 16, (255, 0, 0), SCALE))

    while run:
        clock.tick(FPS)



        for event in pygame.event.get():
            if event.type == SOUNDWAVE:
                x = 500
                y = 500
                # waves.append(SoundWave(x, y, 16, (255, 0, 0, 75), SCALE))
                # # TODO change x, y to location of enemy
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                keydown(event)
            if event.type == TIMER_ZERO:
                print("timer expired")
                reset()
        input()
        draw()
        update()

def main():
    pygame.init()
    intro()
    game()
    pygame.quit()

if __name__ == "__main__":
    main()
