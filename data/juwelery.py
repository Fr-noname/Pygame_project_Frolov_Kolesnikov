import random
# не работает поэтом эти строки кода не учитываю

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
    def help_of_god(self, damage):  # C шансом 50% обнуляет урон
        x = random.randrange(0, 11)
        if x <= 5:
            return 0
        else:
            return damage

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

    def souleater(self, id):  # наносит сущности 500 урона (250 щиту и 250 hp)
        damage = 250
        return damage


class RingOfPower: # Берсерк
    def berserk(self, hp, shield):
        k_out = ((101 - hp) + (50 - shield)) / 4
        return k_out

    def berserk(self):  # Увеличивает урон - в 20, длиться 20 сек
        return 20, 20


class GoldWatch:
    def on_time(self, seconds):  # Если проходишь уровень меньше, чем за 3 мин 20 сек, то щит, hp, атака увеличиваются
        k = 2 - seconds / 100  # на k (например k = 1, hp было 100, стало 200, или k = -1, hp стало 50)
        return k

    def rabbit_hole(self):  # телепортирует на 200 пикселей по напралению взгляда
        return 200


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
