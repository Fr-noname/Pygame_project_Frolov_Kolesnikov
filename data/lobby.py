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
    else:
        image = image.convert_alpha()  # метод для преобразования изображения с сохранением информации о прозрачности
    return image
