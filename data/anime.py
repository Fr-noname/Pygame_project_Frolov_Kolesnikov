import os
import sys

import pygame


def load_image(name, colorkey=None):  # загрузка картинок
    fullname = os.path.join('images', name)  # полное имя файла
    if not os.path.isfile(fullname):  # проверка наличия файла
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)  # записывание картинки в переменную
    if colorkey is not None:
        image = image.convert()  # создаёт новую копию изображения с таким же форматом пикселей, как у экрана
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image
