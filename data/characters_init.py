from data.characters import *
from data.juwelery import *
from data.weapons import *


def berserk_init(player_pos, ALL_SPRITES):
    return Berserk(100, 100, 1.5, 2, 12, Axe, ThrowingAxe, RingOfPower, player_pos,
                   "berserk.png", ALL_SPRITES)


def souleater_init(player_pos, ALL_SPRITES):
    return SoulEater(100, 100, 1, 1, 7, DeathScythle, MysteriousGloves, PrisonOfEyes, player_pos,
                     "LIFESTEALER.png", ALL_SPRITES)


def general_init(player_pos, ALL_SPRITES):
    return General(150, 100, 1, 2.5, 15, Kokorowatary, UnlimitedRuleBook, PlaqueOfGeneral, player_pos,
                   "general.png", ALL_SPRITES)


def egor_init(player_pos, ALL_SPRITES):
    return Egor(100, 150, 1, 2, 15, Book, KubikD4, SecretKubik, player_pos,
                "egor.png", ALL_SPRITES)


def scorpius_init(player_pos, ALL_SPRITES):
    return Berserk(90, 120, 1, 1.5, 18, Vakidzasi, ThrowingKnife, GoldWatch, player_pos,
                   "scorpius.png", ALL_SPRITES)


def paladin_init(player_pos, ALL_SPRITES):
    return Berserk(200, 150, 1, 1, 5, HolyChain, Crucifix, Krest, player_pos,
                   "paladin.png", ALL_SPRITES)
