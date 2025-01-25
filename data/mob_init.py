import random

from data.enemies import Archer, SwordMan, Tank


def archer_lvl1_init(id, pos, ALL_SPRITES):
    a = Archer(id, pos, 1.5, 1, 150, 16, ALL_SPRITES, 'Port_archer (1).png')
    return a


def archer_lvl2_init(id, pos, ALL_SPRITES):
    k = random.choice(['Forest_archer.png', 'Field_Archer.png'])
    a = Archer(id, pos, 1.25, 1.2, 175, 18, ALL_SPRITES, k)
    return a


def archer_lvl3_init(id, pos, ALL_SPRITES):
    a = Archer(id, pos, 1.2, 1.5, 200, 20, ALL_SPRITES, 'magician.png')
    return a


def elite_archer_lvl1_init(id, pos, ALL_SPRITES):
    a = Archer(id, pos, 1.25, 1.2, 200, 20, ALL_SPRITES, 'Port_archer (1).png')
    return a


def elite_archer_lvl2_init(id, pos, ALL_SPRITES):
    k = random.choice(['Forest_archer.png', 'Field_Archer.png'])
    a = Archer(id, pos, 1.2, 1.5, 200, 25, ALL_SPRITES, k)
    return a


def elite_archer_lvl3_init(id, pos, ALL_SPRITES):
    a = Archer(id, pos, 1.1, 1.75, 250, 30, ALL_SPRITES, 'magician.png')
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
    a = Tank(id, pos, 0.6, 1, 20, 5, ALL_SPRITES, 'Port_TANK.png')
    return a


def tank_lvl2_init(id, pos, ALL_SPRITES):
    k = random.choice(['Forest_TANK.png', 'Field_TANK.png'])
    a = Tank(id, pos, 0.5, 1, 20, 7, ALL_SPRITES, k)
    return a


def tank_lvl3_init(id, pos, ALL_SPRITES):
    a = Tank(id, pos, 0.4, 1, 20, 9, ALL_SPRITES, 'BLOB.png')
    return a


def elite_tank_lvl1_init(id, pos, ALL_SPRITES):
    a = Tank(id, pos, 0.5, 1.1, 25, 7, ALL_SPRITES, 'Port_TANK.png')
    return a


def elite_tank_lvl2_init(id, pos, ALL_SPRITES):
    k = random.choice(['Forest_TANK.png', 'Field_TANK.png'])
    a = Tank(id, pos, 0.4, 1.2, 25, 9, ALL_SPRITES, k)
    return a


def elite_tank_lvl3_init(id, pos, ALL_SPRITES):
    a = Tank(id, pos, 0.3, 1.25, 25, 11, ALL_SPRITES, 'BLOB.png')
    return a
