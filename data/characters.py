from data.anime import *
from data.classes import *
from math import *


class Player(pygame.sprite.Sprite):
    def __init__(self, hp, shield, k_in, k_out, v, weapon1, weapon2, juwelery, player_pos, image_name, ALL_SPRITES):
        super().__init__(ALL_SPRITES)
        self.hp = hp
        self.shield = shield
        self.k_in = k_in
        self.k_out = k_out
        self.juwelery = juwelery
        self.v = v
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.w = 0
        self.x = player_pos.x
        self.y = player_pos.y
        self.image = load_image(image_name)
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.px = self.x
        self.py = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def movement(self):
        self.px = self.x
        self.py = self.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.v
        if keys[pygame.K_s]:
            self.y += self.v
        if keys[pygame.K_a]:
            self.x -= self.v
        if keys[pygame.K_d]:
            self.x += self.v
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def incoming_damage(self, damage):
        if self.shield <= 0:
            self.hp -= damage * self.k_in
        else:
            self.shield -= damage * self.k_in

    def get_information(self):
        return [self.hp, self.shield, self.k_in, self.k_out, self.juwelery, self.v]

    def attack(self, *mobs):
        if self.w % 2 == 0:
            for r in mobs:
                x, y = r.get_pos()
                s_to_mob = sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
                if s_to_mob <= self.weapon1.attack():
                    r.incoming_damage(self.weapon1.damage * self.k_out)

        else:
            pass

    def change_weapon(self):
        self.w += 1

    def return_pos(self):
        return [self.x, self.y]

    def update(self):
        if pygame.sprite.spritecollideany(self, KLETKA):
            self.x = self.px
            self.y = self.py


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
