import random


class SecretKubik:  # Для перса Егора
    def multiple_damage(self):  # пасивная способность
        return random.randrange(1, 21)

    def multiple_hp(self):  # пассивная способность
        return random.randrange(1, 21)

    def brosok(self):  # актвная способность, бросает кубик (итоговый урон - size * damage * k_out)
        size = random.randrange(1, 21)
        damage = random.randrange(1, 21)
        return size * damage


class Krest:  # Для паладина
    def help_of_god(self, *negative_effects):  # Увеличивает hp за полученные негативные эффекты, пассивный
        return [len(negative_effects) * 2, []]

    def power_of_paladin(self):  # Примерно, как 2-ая абилка паладина из soul Knight
        pass


class PrisonOfEyes:  # Для Пожирателя душ
    def __init__(self):
        self.kills = 0

    def deal_with_devil(self, hp, shield, k_out, kills):
        k = kills / 20
        if self.kills != kills:
            self.kills = kills
            return [hp * k, shield * k, k_out * k]

    def souleater(self, id):  # наносит сущность 1000 урона (500 щиту и 500 hp)
        damage = 500
        return damage


class RingOfPower:
    def berserk(self, hp, shield):
        k_out = ((101 - hp) + (50 - shield)) / 2
        return k_out

    def berserk(self):  # Увеличивает скорость атаки в 2 раза, урон - в 20
        return 2, 20


class GoldWatch:
    def On_time(self, seconds):  # Если проходишь уровень меньше, чем за 3 минуты, то щит, hp, атака увеличиваются
        k = 2 - seconds / 100  # на k (например k = 1, hp было 100, стало 200, или k = -1, hp стало 50)
        return k

    def rabbit_hole(self):  # телепортирует на 200 пикселей по напралению взгляда
        pass


class PlaqueOfGeneral:
    def __init__(self):
        self.kills = 0

    def hunger(self, k_out, kills):
        k = kills / 10
        if self.kills != kills:
            self.kills = kills
            return k_out * k

    def lord_of_meteorites(self):  # призывает метеорит, наносящий 250 урона
        damage = 250
        return damage

    def gurdian_of_the_east(self):  # Огненная волна, наносящая 250 урона
        damage = 250
        return damage
