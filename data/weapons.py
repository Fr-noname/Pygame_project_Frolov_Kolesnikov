from math import sqrt
from time import sleep


class Weapon:
    def __init__(self, damage, r):  # r - дальность атаки
        self.damage = damage
        self.r = r

    def attack(self):
        return self.r

    def damage(self):
        return self.damage


class Bow:
    def __init__(self, damage, s):
        self.damage = damage
        self.s = s
        self.min_s = 9999999999999999999999999999

    def atack(self, time):
        arrow_damage = self.damage * time
        self.deal_damage(arrow_damage)

    def deal_damage(self, arrow_damage):
        pass


class Kokorowatary(Weapon):  # Перс Никиты
    pass


class UnlimitedRuleBook(Bow):  # Перс Никиты
    pass


class HolyChain(Weapon):  # Паладин
    pass


class Crucifix(Bow):  # Паладин
    pass


class Vakidzasi(Weapon):  # Скорпиус
    pass


class ThrowingKnife(Bow):  # Скорпиус
    pass


class Axe(Weapon):  # Берсерк
    pass


class ThrowingAxe(Bow):  # Берсерк
    pass


class Book(Weapon):  # Егор
    pass


class KubikD4(Bow):  # Егор
    pass


class MysteriousGloves(Bow):  # SoulEater
    pass


class DeathScythle(Weapon):  # SoulEater
    pass
