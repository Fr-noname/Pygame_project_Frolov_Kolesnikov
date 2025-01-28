import random

import pygame

from data.enemies import Archer, SwordMan, Tank


def archer_lvl1_init(id, pos, ALL_SPRITES):
    a = Archer(id, pos, 1.5, 1, 600, 16, ALL_SPRITES, 'Port_archer (1).png')
    return a


def archer_lvl2_init(id, pos, ALL_SPRITES):
    k = random.choice(['Forest_archer.png', 'Field_Archer.png'])
    a = Archer(id, pos, 1.25, 1.2, 650, 18, ALL_SPRITES, k)
    return a


def archer_lvl3_init(id, pos, ALL_SPRITES):
    a = Archer(id, pos, 1.2, 1.5, 700, 20, ALL_SPRITES, 'magician.png')
    return a


def elite_archer_lvl1_init(id, pos, ALL_SPRITES):
    a = Archer(id, pos, 1.25, 1.2, 700, 20, ALL_SPRITES, 'Port_archer (1).png')
    return a


def elite_archer_lvl2_init(id, pos, ALL_SPRITES):
    k = random.choice(['Forest_archer.png', 'Field_Archer.png'])
    a = Archer(id, pos, 1.2, 1.5, 750, 25, ALL_SPRITES, k)
    return a


def elite_archer_lvl3_init(id, pos, ALL_SPRITES):
    a = Archer(id, pos, 1.1, 1.75, 1300, 30, ALL_SPRITES, 'magician.png')
    return a


def swordman_lvl1_init(id, pos, ALL_SPRITES):
    a = SwordMan(id, pos, 1, 1.2, 20, 20, ALL_SPRITES, 'Port_swprdman.png')
    return a


def swordman_lvl2_init(id, pos, ALL_SPRITES):
    k = random.choice(['Forest_Swordman (1).png', 'Field_Swordman.png'])
    a = SwordMan(id, pos, 0.9, 1.25, 20, 25, ALL_SPRITES, k)
    return a


def swordman_lvl3_init(id, pos, ALL_SPRITES):
    a = SwordMan(id, pos, 0.8, 1.5, 20, 30, ALL_SPRITES, 'LIFE_SWORD.png')
    return a


def elite_swordman_lvl1_init(id, pos, ALL_SPRITES):
    a = SwordMan(id, pos, 0.8, 1.5, 25, 30, ALL_SPRITES, 'Port_swprdman.png')
    return a


def elite_swordman_lvl2_init(id, pos, ALL_SPRITES):
    k = random.choice(['Forest_Swordman (1).png', 'Field_Swordman.png'])
    a = SwordMan(id, pos, 0.7, 1.6, 25, 35, ALL_SPRITES, k)
    return a


def elite_swordman_lvl3_init(id, pos, ALL_SPRITES):
    a = SwordMan(id, pos, 0.6, 1.7, 25, 40, ALL_SPRITES, 'LIFE_SWORD.png')
    return a


def tank_lvl1_init(id, pos, ALL_SPRITES):
    a = Tank(id, pos, 0.6, 1, 20, 15, ALL_SPRITES, 'Port_TANK.png')
    return a


def tank_lvl2_init(id, pos, ALL_SPRITES):
    k = random.choice(['Forest_TANK.png', 'Field_TANK.png'])
    a = Tank(id, pos, 0.5, 1, 20, 17, ALL_SPRITES, k)
    return a


def tank_lvl3_init(id, pos, ALL_SPRITES):
    a = Tank(id, pos, 0.4, 1, 20, 19, ALL_SPRITES, 'BLOB.png')
    return a


def elite_tank_lvl1_init(id, pos, ALL_SPRITES):
    a = Tank(id, pos, 0.5, 1.1, 25, 17, ALL_SPRITES, 'Port_TANK.png')
    return a


def elite_tank_lvl2_init(id, pos, ALL_SPRITES):
    k = random.choice(['Forest_TANK.png', 'Field_TANK.png'])
    a = Tank(id, pos, 0.4, 1.2, 25, 19, ALL_SPRITES, k)
    return a


def elite_tank_lvl3_init(id, pos, ALL_SPRITES):
    a = Tank(id, pos, 0.3, 1.25, 25, 21, ALL_SPRITES, 'BLOB.png')
    return a


def Boss_lvl1_init(id, pos, ALL_SPRITES):
    a = Tank(id, pos, 0.2, 1.9, 100, 40, ALL_SPRITES, 'BOSS_PORT.png')
    return a


def Boss_lvl2_init_1(id, pos, ALL_SPRITES):
    a = SwordMan(id, pos, 0.2, 1.9, 100, 40, ALL_SPRITES, 'KOLODA.png')
    print(pos)
    pos_2 = (1920 - pos[0] - 128, 1080 - pos[1] - 128)
    b = Archer(id, pos_2, 0.3, 1.8, 1000, 40, ALL_SPRITES, 'PEN.png')
    return a, b


def Boss_lvl2_init_2(id, pos, ALL_SPRITES):
    a = Tank(id, pos, 0.15, 2, 100, 30, ALL_SPRITES, 'Field_BOSS.png')
    return a


def Boss_lvl3_init(id, pos, ALL_SPRITES):
    a = Tank(id, pos, 0.1, 2.5, 150, 45, ALL_SPRITES, 'MIMIC.png')
    return a
