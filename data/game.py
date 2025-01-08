import pygame
from pygame import QUIT, Color, Surface

from data import functions
from data import lobby
from data.functions import Pixel
from levels.rooms import Room1


def start(setings=[1]):
    pygame.init()  # Инициация PyGame
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Until it Done")
    background = Surface((1920, 1080))
    background.fill((0, 0, 255))
    running = True
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False
    x = y = 0
    for row in Room1:
        for col in row:
            if col == "-":
                background = Surface((20, 20))
                background.fill((255, 255, 0))
                screen.blit(background, (x, y))

            x += 20
        y += 20
        x = 0

    while running:
        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
        screen.blit(background, (0, 0))
        pygame.display.update()


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
