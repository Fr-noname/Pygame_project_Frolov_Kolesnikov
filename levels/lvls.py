import random
from data.mob_init import *
from data.functions import *
from levels.rooms import *
from data.classes import KLETKA

# Списки комнат:
BEG_ROOMS = [beg_room1, beg_room2, beg_room3]  # стартовых
BATTLE_ROOMS = [battle_room1_l_v, battle_room2_r_l, battle_room3_l_n, battle_room4_r_v, battle_room5_r_n]  # с мобами
BOSS_ROOMS = [battle_room2_r_l, battle_room3_l_n]  # с боссом


def lvl(n, screen, room, ALL_SPRITES, kills, lvl_nomer, difficulty_nomer):  # генерация уровня
    if room % 5 == 1:  # стартовая комната
        name = random.choice(BEG_ROOMS)
        s = generate_lvl(name, screen, n, ALL_SPRITES)
    elif room % 5 == 0 and kills // 30 >= 1:  # комната с мобами
        name = random.choice(BOSS_ROOMS)
        s = generate_lvl(name, screen, n, ALL_SPRITES)
    else:  # комната босса
        name = random.choice(BATTLE_ROOMS)
        s = generate_lvl(name, screen, n, ALL_SPRITES)
    try:
        mobs = generate_mobs(ALL_SPRITES, lvl_nomer, s, difficulty_nomer, room)  # генерация мобов
    except Exception:
        print("Что-то умерло при генерации мобов")
    return s, mobs

