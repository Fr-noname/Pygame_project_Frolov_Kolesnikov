import os
import sys

import pygame


def lobby():
    pygame.init()
    size = w, h = (2560, 1440)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True

    dt = 0

    player_pos = pygame.Vector2(w // 2 + 1, h // 2 + 1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("Black")
    pygame.quit()


