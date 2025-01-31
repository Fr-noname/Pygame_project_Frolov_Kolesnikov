from math import sqrt

import pygame

from data.anime import *
from data.sprite_groups import KLETKA


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, w, h):
        self.dx = 0
        self.dy = 0
        self.w = w
        self.h = h

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self.w // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - self.h // 2)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, ALL_SPRITES):
        super().__init__(ALL_SPRITES)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width // columns, sheet.get_height // rows)
        for r in range(rows):
            for t in range(columns):
                frame_location = (self.rect.x * r, self.rect.y * t)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Border(pygame.sprite.Sprite):
    def __init__(self, x, y, image_name, ALL_SPRITES):
        super().__init__(ALL_SPRITES)
        self.add(KLETKA)
        self.image = load_image(image_name)
        self.rect = pygame.Rect(x, y, 20, 20)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, ALL_SPRITES, mob, damage, creator):
        super().__init__(ALL_SPRITES)
        min_s = 9999
        self.mob = mob
        self.sprites = ALL_SPRITES
        self.damage = damage
        self.creator = creator
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = (mob.x - x) // 200
        self.vy = (mob.y - y) // 200

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)

        if pygame.sprite.spritecollideany(self, KLETKA):
            self.damage = 0
            self.kill()
        spisok = pygame.sprite.spritecollideany(self, self.sprites)
        print(spisok, self.creator)
        if self.creator != spisok and spisok != self:
            if spisok:
                self.mob.incoming_damage(self.damage)
                self.damage = 0
                self.kill()
