import random

from data.functions import *
from levels.rooms import *

KILLS_ON_LVL = 0
BEG_ROOMS = [beg_room1, beg_room2, beg_room3]
BATTLE_ROOMS = [battle_room1_l_v, battle_room2_r_l, battle_room3_l_n, battle_room4_r_v, battle_room5_r_n]
BOSS_ROOMS = [battle_room2_r_l, battle_room3_l_n]


def lvl(n, screen, room, ALL_SPRITES):
    if room % 5 == 1:
        name = random.choice(BEG_ROOMS)
        s = generate_lvl(name, screen, n, ALL_SPRITES)
    elif room % 5 == 0 and KILLS_ON_LVL <= 30:
        name = random.choice(BOSS_ROOMS)
        s = generate_lvl(name, screen, n, ALL_SPRITES)
    else:
        name = random.choice(BATTLE_ROOMS)
        s = generate_lvl(name, screen, n, ALL_SPRITES)
    return s
