
from data import functions
import pygame


def lobby():
    pygame.init()
    image = functions.load_image('lobby.png')
    size = w, h = (1920, 1080)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True

    dt = 0

    player_pos = pygame.Vector2(w // 2 + 1, h // 2 + 1)
    screen.blit(image, (1, 1))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

        screen.fill("Black")
    pygame.quit()


