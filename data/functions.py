import random
import pygame

from data.mob_init import *

PIXEL = (20, 20)


def generate_lvl(name, screen, n, ALL_SPRITES):
    x = y = 0
    s = []
    if n == 2:
        wall = random.choice(['lvl2_field_wall.png', 'lvl2_forest_wall.png'])
    for row in name:
        for col in row:
            if col == "-":
                if n == 1:
                    from data.classes import Border
                    a = Border(x, y, 'lvl1_wall.png', ALL_SPRITES)
                elif n == 3:
                    from data.classes import Border
                    a = Border(x, y, 'lvl3_wall.png', ALL_SPRITES)
                else:
                    from data.classes import Border
                    a = Border(x, y, wall, ALL_SPRITES)
            else:
                s.append([x, y])
                background = pygame.Surface(PIXEL)
                background.fill((0, 0, 0))
                screen.blit(background, (x, y))
            x += PIXEL[0]
        y += PIXEL[1]
        x = 0
        pygame.display.update()
        pygame.display.flip()
    return s


def generate_mobs(ALL_SPRITES, lvl, s):
    spisok = []
    for i in range(7):
        pos = random.choice(s)
        while pos[0] >= 1920 - 128 or pos >= 1080 - 128:
            pos = random.choice(s)
        if lvl == 1:
            a = random.randrange(0, 2)
            if a % 3 == 0:
                s = archer_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
        if lvl == 2:
            a = random.randrange(0, 2)
            if a % 3 == 0:
                s = archer_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
        if lvl == 3:
            a = random.randrange(0, 2)
            if a % 3 == 0:
                s = archer_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
        spisok.append(s)
    return spisok


global DifficultyNomer
DifficultyNomer = 1

Pixel = (20, 20)
