import pygame
from World import World
from global_constants import *

FPS = 60
SCALE = 3
WIDTH, HEIGHT = ROOM_DIM[0] * TILESIZE, ROOM_DIM[1] * TILESIZE

WIN = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
pygame.display.set_caption("Miel Monteur saves the world")

world = World()


def draw():
    temp_win = pygame.Surface((WIDTH, HEIGHT))
    world.draw(temp_win)
    temp_win = pygame.transform.scale(temp_win, (WIDTH * 3, HEIGHT * 3))
    WIN.blit(temp_win, (0, 0))
    pygame.display.update()


def update():
    pass


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
                        print("hi")
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
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    world.move(1)
                if event.key == pygame.K_RIGHT:
                    world.move(2)
                if event.key == pygame.K_DOWN:
                    world.move(3)
                if event.key == pygame.K_LEFT:
                    world.move(4)
                if event.key == pygame.K_ESCAPE:
                    pause()

        update()
        draw()


def main():
    intro()
    game()
    pygame.quit()


if __name__ == "__main__":
    main()
