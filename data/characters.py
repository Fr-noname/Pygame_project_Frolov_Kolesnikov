class Player:
    def __init__(self, hp, shield, k_in, k_out, v, weapon, juwelery):
        self.hp = hp
        self.shield = shield
        self.k_in = k_in
        self.k_out = k_out
        self.juwelery = juwelery
        self.v = v
        self.weapon = weapon

    def movement(self):
        pass

    def taking_damage(self, damage):
        if self.shield <= 0:
            self.hp -= damage * self.k_in
        else:
            self.shield -= damage * self.k_in

    def get_information(self):
        return [self.hp, self.shield, self.k_in, self.k_out, self.juwelery, self.v]

    def dealing_damage(self):
        pass

    def death(self):
        pass


class Egor(Player):
    pass


class Berserk(Player):
    pass


class SoulEater(Player):
    pass


class Scorpius(Player):
    pass


class Paladin(Player):
    pass


class General(Player):
    pass
