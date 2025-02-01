from data.characters import *
from data.juwelery import *
from data.weapons import *


def berserk_init(player_pos, ALL_SPRITES):
    return Berserk(150, 100, 1.4, 3, 12, Axe(25, 100), ThrowingAxe(20, 20), RingOfPower, player_pos,
                   "BLOB.png", ALL_SPRITES)


def souleater_init(player_pos, ALL_SPRITES):
    return SoulEater(100, 100, 1, 1, 7, DeathScythle(40, 90), MysteriousGloves(30, 20), PrisonOfEyes, player_pos,
                     "LIFESTEALER.png", ALL_SPRITES)


def general_init(player_pos, ALL_SPRITES):
    return General(150, 100, 1, 2.5, 15, Kokorowatary(30, 90), UnlimitedRuleBook(25, 25), PlaqueOfGeneral, player_pos,
                   "general.png", ALL_SPRITES)


def egor_init(player_pos, ALL_SPRITES):
    return Egor(100, 150, 1, 2, 15, Book(15, 100), KubikD4(25, 25), SecretKubik, player_pos,
                "BLOB.png", ALL_SPRITES)


def scorpius_init(player_pos, ALL_SPRITES):
    return Scorpius(90, 120, 1, 1.5, 18, Vakidzasi(30, 150), ThrowingKnife(40, 15), GoldWatch, player_pos,
                    "scorpius.png", ALL_SPRITES)


def paladin_init(player_pos, ALL_SPRITES):
    return Paladin(200, 150, 0.1, 1.2, 5, HolyChain(50, 120), Crucifix(40, 30), Krest, player_pos,
                   "paladin.png", ALL_SPRITES)
