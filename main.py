import pygame
from data import lobby

if __name__ == "__main__":
    lobby.lobby()


import os
import sys
from random import randrange, randint

import pygame

ALL_SPRITES = pygame.sprite.Group()
HORISONTAL_BOARDERS = pygame.sprite.Group()
VERTICAL_BOARDERS = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(ALL_SPRITES)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        while 1:
            self.vx = randint(-5, 5)
            self.vy = randrange(-5, 5)
            if self.vx and self.vy:
                break

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, HORISONTAL_BOARDERS):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, VERTICAL_BOARDERS):
            self.vx = -self.vx


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(ALL_SPRITES)
        if x1 == x2:  # вертикальная стенка
            self.add(VERTICAL_BOARDERS)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(HORISONTAL_BOARDERS)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


def main():
    # pygame setup
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)

    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)


    for _ in range(10):
        Ball(25, 400, 400)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ALL_SPRITES.update(event)
        screen.fill("white")
        # RENDER YOUR GAME HERE
        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update()
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
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


if __name__ == '__main__':
    main()
