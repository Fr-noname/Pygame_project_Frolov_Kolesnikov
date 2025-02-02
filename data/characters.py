from data.anime import *
from data.classes import *
from math import *


class Player(pygame.sprite.Sprite):  # основной класс игрока
    def __init__(self, hp, shield, k_in, k_out, v, weapon1, weapon2, juwelery, player_pos, image_name, ALL_SPRITES):
        super().__init__(ALL_SPRITES)
        self.hp = hp  # прсваивание значений Хп, Щита, оружия, Ювелирки (не работает, строки кода для неё не учитываем)
        self.shield = shield  # позиции, спрайта, коэффициентов наносимого и получаемого урона
        self.k_in = k_in
        self.k_out = k_out
        self.juwelery = juwelery
        self.v = v
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.x = player_pos.x
        self.y = player_pos.y
        self.image = load_image(image_name)
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.px = self.x
        self.py = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def movement(self):  # передвижение игрока
        self.px = self.x
        self.py = self.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:  # вверх
            self.y -= self.v
        if keys[pygame.K_s]:  # вниз
            self.y += self.v
        if keys[pygame.K_a]:  # влево
            self.x -= self.v
        if keys[pygame.K_d]:  # вправо
            self.x += self.v
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def incoming_damage(self, damage):  # получение урона игроком
        if self.shield <= 0:
            self.hp -= damage * self.k_in  # урон по щиту (если он есть)
        else:
            self.shield -= damage * self.k_in  # урон по Хп
        print(self.shield, self.hp)

    def attack(self, mobs, ALL_SPRITES, w):  # Атака
        if mobs:  # Есть ли противники
            if w % 2 == 0:  # ближняя атака
                for r in mobs:  # пробежка по мобам
                    x, y = r.get_pos()
                    s_to_mob = sqrt((self.x - x) ** 2 + (self.y - y) ** 2)  # расчет расстояния до моба
                    if s_to_mob <= self.weapon1.attack():  # получение урона, если моб в зоне поражения
                        r.incoming_damage(self.weapon1.damage * self.k_out)

            else:
                min_s = 9999
                for r in mobs:  # ближайший моб
                    x, y = r.get_pos()
                    if sqrt((r.x - x) ** 2 + (r.y - y) ** 2) <= min_s:  # расчет расстояния до моба
                        mob = r  # ближайший моб
                bullet = Bullet(self.weapon2.s // 2, self.x, self.y, ALL_SPRITES, mob,
                                self.weapon2.damage * self.k_out, self)  # генерация пули

    def return_pos(self):  # получение координат игрока
        return [self.x, self.y]

    def update(self):  # обновление и взаимодействие со стеной
        if pygame.sprite.spritecollideany(self, KLETKA):
            self.x = self.px
            self.y = self.py


class Egor(Player):  # класс егора
    pass


class Berserk(Player):  # класс берсерка
    pass


class SoulEater(Player):  # класс пожирю душ
    pass


class Scorpius(Player):  # класс скорпиуса
    pass


class Paladin(Player):  # класс паладина
    pass


class General(Player):  # класс генерала
    pass
