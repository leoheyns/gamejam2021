import pygame
from World import World

WIDTH, HEIGHT = 1024, 576
FPS = 60


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("wie dit leest trekt een ad")

world = World()

def draw():
    world.draw(WIN)
    pygame.display.update()


def update():
    pass

def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        update()
        draw()
    pygame.quit()

if __name__ == "__main__":
    main()