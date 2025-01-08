import pygame

from data import functions
from data import lobby


def start(setings=[1]):
    pygame.init()
    size = w, h = (1920, 1080)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    screen.fill((0, 0, 0))
    while running:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)


def setings():
    pygame.init()
    image = functions.load_image('difficulty.png')
    size = w, h = (1920, 1080)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    screen.blit(image, (1, 1))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if 50 <= int(pos[0]) <= 1025:
                    if 400 <= int(pos[1]) <= 475:
                        functions.DifficultyNomer = 1
                        running = False
                    elif 525 <= int(pos[1]) <= 600:
                        functions.DifficultyNomer = 2
                        running = False
                    elif 650 <= int(pos[1]) <= 725:
                        functions.DifficultyNomer = 3
                        running = False
        screen.blit(image, (1, 1))
        pygame.display.flip()
    pygame.quit()
    lobby.lobby()
