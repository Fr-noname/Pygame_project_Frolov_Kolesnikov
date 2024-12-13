from data.enemies import Archer, SwordMan, Tank


def archer_lvl1_init(id, pos):
    a = Archer(id, pos, 1.5, 1, 150, 16)
    return a


def archer_lvl2_init(id, pos):
    a = Archer(id, pos, 1.25, 1.2, 175, 18)
    return a


def archer_lvl3_init(id, pos):
    a = Archer(id, pos, 1.2, 1.5, 200, 20)
    return a


def elite_archer_lvl1_init(id, pos):
    a = Archer(id, pos, 1.25, 1.2, 200, 20)
    return a


def elite_archer_lvl2_init(id, pos):
    a = Archer(id, pos, 1.2, 1.5, 200, 25)
    return a


def elite_archer_lvl3_init(id, pos):
    a = Archer(id, pos, 1.1, 1.75, 250, 30)
    return a


def swordman_lvl1_init(id, pos):
    a = SwordMan(id, pos, 1, 1.2, 20, 20)
    return a


def swordman_lvl2_init(id, pos):
    a = SwordMan(id, pos, 0.9, 1.25, 20, 25)
    return a


def swordman_lvl3_init(id, pos):
    a = SwordMan(id, pos, 0.8, 1.5, 20, 30)
    return a


def elite_swordman_lvl1_init(id, pos):
    a = SwordMan(id, pos, 0.8, 1.5, 25, 30)
    return a


def elite_swordman_lvl2_init(id, pos):
    a = SwordMan(id, pos, 0.7, 1.6, 25, 35)
    return a


def elite_swordman_lvl3_init(id, pos):
    a = SwordMan(id, pos, 0.6, 1.7, 25, 40)
    return a


def tank_lvl1_init(id, pos):
    a = Tank(id, pos, 0.6, 1, 20, 15)
    return a


def tank_lvl2_init(id, pos):
    a = Tank(id, pos, 0.5, 1, 20, 17)
    return a


def tank_lvl3_init(id, pos):
    a = Tank(id, pos, 0.4, 1, 20, 19)
    return a


def elite_tank_lvl1_init(id, pos):
    a = Tank(id, pos, 0.5, 1.1, 25, 17)
    return a


def elite_tank_lvl2_init(id, pos):
    a = Tank(id, pos, 0.4, 1.2, 25, 19)
    return a


def elite_tank_lvl3_init(id, pos):
    a = Tank(id, pos, 0.3, 1.25, 25, 21)
    return a
