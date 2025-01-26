import random
from math import sqrt
import pygame
from data.classes import *
from data.anime import *
from data.sprite_groups import KLETKA


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

    def damaging(self, player, ALL_SPRITES):
        a = random.randrange(0, 25)
        if a == 0:
            pos = player.return_pos()
            s_to_player = sqrt((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2)
            if s_to_player <= self.radius:
                player.incoming_damage(self.damage * self.k_out)

    def incoming_damage(self, damage):
        if self.shield <= 0:
            self.hp -= damage * self.k_in
        else:
            self.shield -= damage * self.k_in
        print(self.shield, self.hp)

    def move_to_player(self, player_pos):
        pass

    def get_inf(self):
        return self.hp, self.shield

    def death(self):
        return self.id

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
            x = random.choice([-1, 1])
            self.x += x * 20
        if pygame.sprite.spritecollideany(self, KLETKA):
            self.x = self.px
        if pygame.sprite.spritecollideany(self, KLETKA):
            y = random.choice([-1, 1])
            self.y += y * 20
        if pygame.sprite.spritecollideany(self, KLETKA):
            self.y = self.py

            # self.x = self.px
            # self.y = self.py
            # self.x += 10
            # if pygame.sprite.spritecollideany(self, KLETKA):
            #     self.x = self.px
            #     self.y += 10
            #     if pygame.sprite.spritecollideany(self, KLETKA):
            #         self.y = self.py
            #     else:
            #         self.y += 10
            # else:
            #     self.x += 10
    def get_pos(self):
        return self.x, self.y


class Archer(Enemy):
    def damaging(self, player, ALL_SPRITES):
        rand = random.randrange(0, 200)
        if rand == 0:
            x = player.x
            y = player.y
            if x >= self.x and y >= self.y:
                bullet = Bullet(10, self.x + 168, self.y + 168, ALL_SPRITES, player,
                                self.damage * self.k_out, self)
            if x <= self.x and y >= self.y:
                bullet = Bullet(10, self.x - 40, self.y + 168, ALL_SPRITES, player,
                                self.damage * self.k_out, self)
            if x >= self.x and y <= self.y:
                bullet = Bullet(10, self.x + 168, self.y - 40, ALL_SPRITES, player,
                                self.damage * self.k_out, self)
            if x <= self.x and y <= self.y:
                bullet = Bullet(10, self.x - 40, self.y - 40, ALL_SPRITES, player,
                                self.damage * self.k_out, self)


class Tank(Enemy):
    pass


class SwordMan(Enemy):
    pass
