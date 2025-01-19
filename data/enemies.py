import random
from math import sqrt
import pygame
from data.anime import *
from data.classes import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, id, position, k_in, k_out, r, dam, ALL_SPRITES, image_name):
        # k_in - то, сколько % урона получает моб, r - радиус атаки.
        super().__init__(ALL_SPRITES)
        self.mob_pos = pygame.Vector2(position)
        self.image = load_image(image_name)
        self.id = id
        self.hp = 100
        self.shield = 50
        self.k_in = k_in
        self.k_out = k_out  # k_out - то, сколько % урона получает игрок от моба
        self.radius = r
        self.damage = dam
        self.min_s = 9999999999999999999999999999
        self.archer_id = 0
        self.s_to_player = 0
        self.x = self.mob_pos.x
        self.y = self.mob_pos.y
        self.px = self.x
        self.py = self.y
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def atack(self, player_pos):
        s_to_player = sqrt((int(player_pos[0]) - int(self.mob_pos[0])) ** 2 + (int(player_pos[1])
                                                                               - int(self.mob_pos[1])) ** 2)
        if s_to_player <= self.radius:
            self.damaging()

    def damaging(self):
        pass

    def incoming_damage(self, damage):
        if self.shield <= 0:
            self.hp -= damage * self.k_in
        else:
            self.shield -= damage * self.k_in

    def move_to_player(self, player_pos):
        pass

    def get_inf(self):
        return self.hp, self.shield

    def death(self):
        pass

    def movemnt(self, player_pos):
        self.px = self.x
        self.py = self.y
        vx = (player_pos[0] - self.x) // 60
        vy = (player_pos[1] - self.y) // 60
        self.x += vx
        self.y += vy
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def get_id(self):
        return self.id

    def update(self):
        if pygame.sprite.spritecollideany(self, KLETKA):
            self.x = self.px
            self.y = self.py
            self.x += 10
            if pygame.sprite.spritecollideany(self, KLETKA):
                self.x = self.px
                self.y += 10
                if pygame.sprite.spritecollideany(self, KLETKA):
                    self.y = self.py
                else:
                    self.y += 10
            else:
                self.x += 10


class Archer(Enemy):
    def damaging(self):
        a = random.randrange(0, 4)
        dam = random.randrange(self.damage)
        if a == 0:  # Попал
            pass
        else:  # не попал
            pass


class Tank(Enemy):
    def damaging(self):
        a = random.randrange(10, self.damage)
        return a * self.k_out

    def koords_of_archer(self, *spisok_of_koords_and_id, player_pos):
        self.s_to_player = sqrt(
            (int(player_pos[0]) - int(self.pos[0])) ** 2 + (int(player_pos[1]) - int(self.pos[1])) ** 2)
        for r in spisok_of_koords_and_id:
            s_to_archer = sqrt((int(r[0]) - int(self.pos[0])) ** 2 +
                               (int(r[1]) - int(self.pos[1])) ** 2)
            if s_to_archer < self.min_s:
                self.min_s = s_to_archer
                self.archer_id = r[2]

    def movement(self, player_pos):
        pass


class SwordMan(Enemy):
    def damaging(self):
        a = random.randrange(10, self.damage)
        return a
