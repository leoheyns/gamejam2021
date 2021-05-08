from Player import Player
import pygame
from World import World

WIDTH, HEIGHT = 1024, 576
FPS = 60


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("wie dit leest trekt een ad")

world = World()

sprite_group = pygame.sprite.Group()
player = Player()
sprite_group.add(player)

def draw():
    world.draw(WIN)
    sprite_group.draw(WIN)
    pygame.display.update()


def update():
    pass

def input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.move_up()
        pass
    elif keys[pygame.K_s]:
        player.move_down()
        pass
    if keys[pygame.K_a]:
        player.move_left()
        pass
    elif keys[pygame.K_d]:
        player.move_right()
        pass

def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        input()
        update()
        draw()
    pygame.quit()

if __name__ == "__main__":
    main()