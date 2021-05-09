from Player import Player
import pygame

from World import World
from Timer import Timer
from global_constants import *
import copy


FPS = 60

WIN = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
pygame.display.set_caption("wie dit leest trekt een ad")

world = World()
timer = Timer(FPS * 60)

sprite_group = pygame.sprite.Group()
player = Player()
sprite_group.add(player)

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
    player.reset()
    timer.start()

    for room in world.room_dict.values():
        for enemy in room.enemies:
            enemy.waves = []


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

def info():
    titlescreen = pygame.image.load('sprites/GameJam Info Screen.png')
    titlescreen = pygame.transform.scale(titlescreen, (WIDTH * 3, HEIGHT * 3))
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = "You are the great Miel Monteur. The planet is invaded by minions that emit dangerous sound waves. "


    textsurface = font.render(text, False, (255, 255, 255))
    text2 = "You only have one weapon, a wall that you can put between yourself and the sound wave."
    textsurface1 = font.render(text2, False, (255, 255, 255))
    text3 = "Collect the four instruments on the map and destroy the evil minions."
    textsurface2 = font.render(text3, False, (255, 255, 255))
    clock = pygame.time.Clock()
    info = True
    while info:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if 1368 <= x <= 1500:
                    if 13 <= y <= 126:
                        return
        WIN.blit(titlescreen, (0, 0))
        WIN.blit(textsurface, (80, HEIGHT * 1.2))
        WIN.blit(textsurface1, (80, (HEIGHT * 1.2)+50))
        WIN.blit(textsurface2, (80, (HEIGHT * 1.2)+100))
        pygame.display.update()
        clock.tick(FPS)


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
                print(x, y)
                if 520 <= y <= 670:
                    if 110 <= x <= 515:
                        return
                    if 1015 <= x <= 1430:
                        pygame.quit()
                        quit()
                if 710 <= y <= 853:
                    if 563 <= x <= 972:
                        info()

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

    while run:
        clock.tick(FPS)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                keydown(event)
            if event.type == TIMER_ZERO:
                print("timer expired")
                reset()

        for enemy in world.get_current_room().enemies:
            for wave in enemy.waves:
                if wave.on_miel(player.current_pos[0], player.current_pos[1]):
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
