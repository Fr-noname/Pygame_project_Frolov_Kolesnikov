from math import sqrt
from time import sleep


class Weapon:
    def __init__(self, damage, attack_speed, r, s, name):  # r - дальность атаки, s - толщина
        self.damage = damage
        self.attack_speed = attack_speed
        self.r = r
        self.s = s
        self.min_s = 9999999999999999999999999999
        self.name = name

    def atack(self, spisok_mob_id, player_pos):
        self.min_s = 9999999999999999999999999999
        min_id = 0
        for i in spisok_mob_id:
            id = i[0]
            x, y = i[1]
            s_to_mob = sqrt((int(player_pos[0]) - int(x)) ** 2 +
                            (int(player_pos[1]) - int(y) ** 2))
            if s_to_mob <= self.min_s:
                self.min_s = s_to_mob
                min_id = id
        if self.min_s <= self.r:
            self.deal_damage(min_id)

    def deal_damage(self, id):
        pass

    def kd(self):
        sleep(1 / self.attack_speed)


class Bow(Weapon):
    def __init__(self, damage, attack_speed, r, s):
        super().__init__()
        self.damage = damage
        self.attack_speed = attack_speed
        self.r = r
        self.s = s
        self.min_s = 9999999999999999999999999999

    def atack(self, time):
        arrow_damage = self.damage * time
        self.deal_damage(arrow_damage)

    def deal_damage(self, arrow_damage):
        pass


class Kokorowatary(Weapon):  # Перс Никиты
    pass


class UnlimitedRuleBook(Weapon):  # Перс Никиты
    pass


class HolyChain(Weapon):  # Паладин
    pass


class Crucifix(Weapon):  # Паладин
    pass


class Vakidzasi(Weapon):  # Скорпиус
    pass


class ThrowingKnife(Weapon):  # Скорпиус
    pass


class Axe(Weapon):  # Берсерк
    pass


class ThrowingAxe(Weapon):  # Берсерк
    pass


class Book(Weapon):  # Егор
    pass


class KubikD4(Weapon):  # Егор
    pass


class MysteriousGloves(Weapon):  # SoulEater
    pass


class DeathScythle(Weapon):  # SoulEater
    pass
