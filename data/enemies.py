import random
from math import sqrt


class Enemy:
    def __init__(self, id, position, k_in, k_out, r, dam):  # k_in - то, сколько % урона получает моб, r - радиус атаки.
        self.id = id
        self.pos = position
        self.hp = 100
        self.shield = 50
        self.k_in = k_in
        self.k_out = k_out  # k_out - то, сколько % урона получает игрок от моба
        self.radius = r
        self.damage = dam
        self.min_s = 9999999999999999999999999999
        self.archer_id = 0

    def atack(self, player_pos):
        s_to_player = sqrt((int(player_pos[0]) - int(self.pos[0])) ** 2 + (int(player_pos[1]) - int(self.pos[1])) ** 2)
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

    def movemnt(self, player_pos):
        s_to_player = sqrt((int(player_pos[0]) - int(self.pos[0])) ** 2 + (int(player_pos[1]) - int(self.pos[1])) ** 2)
        if self.hp == 100:
            if s_to_player < self.radius // 3 + 1:
                a = random.randrange(0, 5)
                if a == 0:
                    pass
                else:
                    pass
            elif self.r >= s_to_player >= self.radius // 3 + 1:
                a = random.randrange(0, 10)
                if a == 0:
                    self.atack()
            else:
                if s_to_player <= 5 * self.radius:
                    self.move_to_player(player_pos)
        else:
            if s_to_player < self.radius // 2 + 1:
                a = random.randrange(0, 1)
                if a == 0:
                    pass
                else:
                    pass
            elif self.r >= s_to_player >= self.radius // 2 + 1:
                a = random.randrange(0, 5)
                if a == 0:
                    self.damaging()
            else:
                if s_to_player <= self.radius * 5 + self.radius // 2:
                    self.move_to_player(player_pos)

    def get_id(self):
        return self.id


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
        s_to_player = sqrt((int(player_pos[0]) - int(self.pos[0])) ** 2 + (int(player_pos[1]) - int(self.pos[1])) ** 2)
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
