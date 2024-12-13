import random
from math import sqrt


class Enemy:
    def __init__(self, id, position, k_in, k_out, r):  # k_in - то, сколько % урона получает моб, r - радиус атаки.
        self.id = id
        self.pos = position
        self.hp = 100
        self.shield = 50
        self.k_in = k_in
        self.k_out = k_out  # k_out - то, сколько % урона получает игрок от моба
        self.radius = r

    def atack(self, player_pos):
        if sqrt(int(player_pos[0]) ** 2 + int(player_pos[1]) ** 2) <= self.radius:
            self.damaging()

    def damaging(self):
        pass

    def incoming_damage(self, damage):
        if self.shield <= 0:
            self.hp -= damage * self.k_in
        else:
            self.shield -= damage * self.k_in


class Archer(Enemy):
    def damaging(self):
        a = random.randrange(0, 2)
        if a != 0:
            pass
        else:
            pass
