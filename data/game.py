import pygame
from pygame import QUIT, Color, Surface

from data import functions
from data import lobby
from data.functions import Pixel
from levels.rooms import Room1
from data import characters


def start(setings=1):
    pygame.init()  # Инициация PyGame
    im = functions.load_image('LIFESTEALER.png', -1)
    player_pos = pygame.Vector2(1, 1)
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Until it Done")
    a = characters.Player(100, 100, 1, 1, 7, None, None, None)
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
                background.fill((255, 0, 255))
                screen.blit(background, (x, y))
            x += 20
        y += 20
        x = 0

    while running:
        background = Surface((1920, 1080))
        background.fill((0, 0, 255))
        x = y = 0
        for row in Room1:
            for col in row:
                screen.blit(im, player_pos)
                if col == "-":
                    background = Surface((20, 20))
                    background.fill((255, 0, 255))
                    screen.blit(background, (x, y))
                else:
                    background = Surface((20, 20))
                    background.fill((0, 0, 0))
                    screen.blit(background, (x, y))
                x += 20
            y += 20
            x = 0

        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                a.attack()
        screen.blit(background, (1, 1))
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            player_pos.y -= a.get_information()[-1]
        if keys[pygame.K_s]:
            player_pos.y += a.get_information()[-1]
        if keys[pygame.K_a]:
            player_pos.x -= a.get_information()[-1]
        if keys[pygame.K_d]:
            player_pos.x += a.get_information()[-1]
        if keys[pygame.K_TAB]:
            a.change_weapon()

        screen.blit(background, (0, 0))
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()


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
