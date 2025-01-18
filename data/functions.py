import os
import random
import sys

import pygame
from pygame import Surface
from data.classes import *
from data.anime import *

PIXEL = (20, 20)


def generate_lvl(name, screen, n):
    x = y = 0
    s = []
    if n == 2:
        wall = random.choice(['lvl2_field_wall.png', 'lvl2_forest_wall.png'])
    for row in name:
        for col in row:
            if col == "-":
                if n == 1:
                    a = Border(x, y, 'lvl1_wall.png')
                elif n == 3:
                    a = Border(x, y, 'lvl3_wall.png')
                else:
                    a = Border(x, y, wall)
            else:
                s.append([x, y])
                background = Surface(PIXEL)
                background.fill((0, 0, 0))
                screen.blit(background, (x, y))
            x += PIXEL[0]
        y += PIXEL[1]
        x = 0
        pygame.display.update()
        pygame.display.flip()
    return s


global DifficultyNomer
DifficultyNomer = 1

Pixel = (20, 20)
