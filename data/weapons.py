from math import sqrt
from time import sleep


class Weapon:
    def __init__(self, damage, attack_speed, r, s, name):  # r - дальность атаки, s - толщина
        self.damaga = damage
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


class Kokorowatary(Weapon):
    pass


class UnlimitedRuleBook(Weapon):
    pass



class HolyChain(Weapon):
    pass


