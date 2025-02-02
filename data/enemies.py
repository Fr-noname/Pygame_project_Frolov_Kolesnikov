import random
from math import sqrt
import pygame
from data.classes import *
from data.anime import *
from data.sprite_groups import KLETKA


class Enemy(pygame.sprite.Sprite):  # основной класс врага
    def __init__(self, id, position, k_in, k_out, r, dam, ALL_SPRITES, image_name):
        # k_in - то, сколько % урона получает моб, r - радиус атаки.
        super().__init__(ALL_SPRITES)  # стандартый процесс записи информации
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

    def atack(self, player_pos):  # атака игрока
        s_to_player = sqrt((int(player_pos[0]) - int(self.mob_pos[0])) ** 2 + (int(player_pos[1])  # изм. раст до игрока
                                                                               - int(self.mob_pos[1])) ** 2)
        if s_to_player <= self.radius:  # если игрок в радиусе атаки, то нанесение урона
            self.damaging()

    def damaging(self, player, ALL_SPRITES):  # нанесение урона
        a = random.randrange(0, 25)  # шанс попадания по игроку
        if a == 0:
            pos = player.return_pos()
            s_to_player = sqrt((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2)  # снова считаем раст. до игрока
            if s_to_player <= self.radius:  # если игрок в радиусе атаки, то он получает урон
                player.incoming_damage(self.damage * self.k_out)

    def incoming_damage(self, damage):  # получение урона
        if self.shield <= 0:
            self.hp -= damage * self.k_in  # по щиту
        else:
            self.shield -= damage * self.k_in  # по Хп
        print(self.shield, self.hp)

    def movemnt(self, player_pos):  # передвижение к игроку
        self.px = self.x
        self.py = self.y
        vx = (player_pos[0] - self.x) // 60
        vy = (player_pos[1] - self.y) // 60
        self.x += vx
        self.y += vy
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self):  # утыкание в стену
        if pygame.sprite.spritecollideany(self, KLETKA):
            self.x = self.px
            self.y = self.py

    def get_pos(self):  # получени позиции моба
        return self.x, self.y


class Archer(Enemy):  # класс лучника
    def damaging(self, player, ALL_SPRITES):  # нанесение урона (аналогичен нанесению урона пулей игроком,
        # но с добавл вероятности выстрела, поэтому коментить не буду)
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


class Tank(Enemy):  # класс танка
    pass


class SwordMan(Enemy):  # класс мечника
    pass
