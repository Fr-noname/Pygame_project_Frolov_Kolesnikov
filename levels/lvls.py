import random
from data.mob_init import *
from data.functions import *
from levels.rooms import *
from data.classes import KLETKA

BEG_ROOMS = [beg_room1, beg_room2, beg_room3]
BATTLE_ROOMS = [battle_room1_l_v, battle_room2_r_l, battle_room3_l_n, battle_room4_r_v, battle_room5_r_n]
BOSS_ROOMS = [battle_room2_r_l, battle_room3_l_n]


def lvl(n, screen, room, ALL_SPRITES, kills, lvl):
    if room % 5 == 1:
        name = random.choice(BEG_ROOMS)
        s = generate_lvl(name, screen, n, ALL_SPRITES)
    elif room % 5 == 0 and kills // 30 >= 1:
        name = random.choice(BOSS_ROOMS)
        s = generate_lvl(name, screen, n, ALL_SPRITES)
    else:
        name = random.choice(BATTLE_ROOMS)
        s = generate_lvl(name, screen, n, ALL_SPRITES)
    # mobs = generate_mobs(1, ALL_SPRITES, lvl, KLETKA)
    mobs = Boss_lvl2_init_1(1, (21, 21), ALL_SPRITES)
    mobs = list(mobs)
    mobs.append(Boss_lvl3_init(1, (500, 900), ALL_SPRITES))
    mobs.append(tank_lvl1_init(1, (900, 500), ALL_SPRITES))
    return s, mobs

