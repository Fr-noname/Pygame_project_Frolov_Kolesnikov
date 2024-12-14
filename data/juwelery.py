import random


class SecretKubik:
    def multiple_damage(self):  # пасивная способность
        return random.randrange(1, 21)

    def multiple_hp(self):  # пассивная способность
        return random.randrange(1, 21)

    def brosok(self):  # актвная способность, бросает кубик (итоговый урон - size * damage)
        size = random.randrange(1, 21)
        damage = random.randrange(1, 21)
        return size * damage


class Krest:
    def help_of_god(self, *negative_effects):  # Увеличивает hp за полученные негативные эффекты, пассивный
        return len(negative_effects) * 2

    def power_of_paladin(self):
        pass