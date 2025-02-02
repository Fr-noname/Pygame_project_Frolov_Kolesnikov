from math import sqrt

import pygame

from data.anime import *
from data.sprite_groups import KLETKA


class Border(pygame.sprite.Sprite):  # класс пикселя (он если что 20 на 20) стены
    def __init__(self, x, y, image_name, ALL_SPRITES):
        super().__init__(ALL_SPRITES)
        self.add(KLETKA)
        self.image = load_image(image_name)
        self.rect = pygame.Rect(x, y, 20, 20)


class Bullet(pygame.sprite.Sprite):  # класс пули
    def __init__(self, radius, x, y, ALL_SPRITES, mob, damage, creator):
        super().__init__(ALL_SPRITES)
        min_s = 9999  # запись радиуса, положения, цели, урона, создателя
        self.mob = mob
        self.sprites = ALL_SPRITES
        self.damage = damage
        self.creator = creator
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)  # создание спрайта пули - кружка
        pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = (mob.x - x) // 200 + 5  # скорость пули
        self.vy = (mob.y - y) // 200 + 5

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)

        if pygame.sprite.spritecollideany(self, KLETKA):  # уничтожение пули о стену
            self.damage = 0
            self.kill()
        elif (self.creator != pygame.sprite.spritecollideany(self, self.sprites)  # попадание в цель
              and pygame.sprite.spritecollideany(self, self.sprites) != self):
            if pygame.sprite.spritecollideany(self, self.sprites):
                self.mob.incoming_damage(self.damage)
                self.damage = 0
                self.kill()
