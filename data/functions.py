import os
import sys

import pygame
from pygame import Surface


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()  # создаёт новую копию изображения с таким же форматом пикселей, как у экрана
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def room_show(room, screen, im, player_pos):
    x = y = 0
    for row in room:
        for col in row:
            if col == "-":
                background = Surface((20, 20))
                background.fill((255, 0, 255))
                screen.blit(background, (x, y))
            else:
                background = Surface((20, 20))
                background.fill((0, 0, 0))
                screen.blit(background, (x, y))
            x += 20
            screen.blit(im, player_pos)
        y += 20
        x = 0
        pygame.display.update()
        pygame.display.flip()


global DifficultyNomer
DifficultyNomer = 1

Pixel = (20, 20)
