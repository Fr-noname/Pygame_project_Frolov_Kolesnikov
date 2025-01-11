import pygame


class Player:
    def __init__(self, hp, shield, k_in, k_out, v, weapon1, weapon2, juwelery):
        self.hp = hp
        self.shield = shield
        self.k_in = k_in
        self.k_out = k_out
        self.juwelery = juwelery
        self.v = v
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.w = 0

    def movement(self, player_pos):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_pos.y -= 10
        if keys[pygame.K_DOWN]:
            player_pos.y += 10
        if keys[pygame.K_LEFT]:
            player_pos.x -= 10
        if keys[pygame.K_RIGHT]:
            player_pos.x += 10

    def taking_damage(self, damage):
        if self.shield <= 0:
            self.hp -= damage * self.k_in
        else:
            self.shield -= damage * self.k_in

    def get_information(self):
        return [self.hp, self.shield, self.k_in, self.k_out, self.juwelery, self.v]

    def attack(self):
        if self.w % 2 == 0:
            pass
        else:
            pass

    def death(self):
        pass

    def change_weapon(self):
        self.w += 1


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
