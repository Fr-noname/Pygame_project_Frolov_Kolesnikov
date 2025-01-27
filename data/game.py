import pygame
import sys

from data import characters
from data import lobby
from data.anime import *
from levels.lvls import *
from data.characters_init import *
from data.mob_init import *


def start(setings=1, room=1, lvl_nomer=1, player=None, ALL_SPRITES=None):
    pygame.init()  # Инициация PyGame
    kills = 30
    flag = False
    size = (1920, 1080)
    player_pos = pygame.Vector2(size[0] // 2, size[1] // 2)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Until it Done")
    clock = pygame.time.Clock()
    fps = 120
    screen.fill((0, 0, 0))

    running = True

    s, mobs = lvl(lvl_nomer, screen, room, ALL_SPRITES, kills, lvl_nomer)

    player.x = 960
    player.y = 540

    while running:
        screen.fill("0x000000")
        for r in s:
            b = pygame.Surface((20, 20))
            b.fill((0, 0, 0))
            screen.blit(b, r)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    player.attack(mobs, ALL_SPRITES=ALL_SPRITES, w=0)
                if e.button == 3:
                    player.attack(mobs, ALL_SPRITES=ALL_SPRITES, w=1)

        # for r in list(mobs):
        #     if r.hp <= 0:
        #         r.kill()
        if mobs.hp <= 0:  # тест моб
            mobs.kill()

        if player.hp <= 0:
            player.kill()
            running = False

        player.movement()
        if mobs.hp > 0:
            mobs.movemnt(player.return_pos())  # тест моб
        # for mob_test in mobs:
        #     mob_test.movemnt(a.return_pos())

        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update()

        mobs.damaging(player, ALL_SPRITES=ALL_SPRITES)

        pos = player.return_pos()
        if int(pos[0]) <= -50 or int(pos[0]) >= 1920 or int(pos[1]) <= -50 or int(pos[1]) >= 1080:
            room += 1
            flag = True
            running = False

        pygame.display.update()
        pygame.display.flip()
        # print(clock.get_fps())
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
    if flag:
        for r in ALL_SPRITES:
            r.kill()

        if room % 5 == 1 and kills // 30 >= 1:
            lvl_nomer += 1

        start(room=room, lvl_nomer=lvl_nomer, player=player, ALL_SPRITES=ALL_SPRITES)
    sys.exit()


def setings():
    pygame.init()
    image = load_image('difficulty.png')
    size = w, h = (1920, 1080)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    screen.blit(image, (1, 1))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if 50 <= int(pos[0]) <= 1025:
                    if 400 <= int(pos[1]) <= 475:
                        DifficultyNomer = 1
                        running = False
                    elif 525 <= int(pos[1]) <= 600:
                        DifficultyNomer = 2
                        running = False
                    elif 650 <= int(pos[1]) <= 725:
                        DifficultyNomer = 3
                        running = False
        screen.blit(image, (1, 1))
        pygame.display.flip()
    pygame.quit()
    lobby.lobby()


def choose_of_character():
    pygame.init()  # Инициация PyGame
    size = (1920, 1080)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Until it Done")
    image = load_image('characters.png')
    clock = pygame.time.Clock()
    fps = 120
    screen.fill((0, 0, 0))
    running = True
    screen.blit(image, (1, 1))
    ALL_SPRITES = pygame.sprite.Group()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                a = False
                player_pos = pygame.Vector2(960, 520)
                if 64 <= int(pos[0]) <= 457 and 247 <= int(pos[1]) <= 313:
                    a = paladin_init(player_pos, ALL_SPRITES=ALL_SPRITES)
                elif 619 <= int(pos[0]) <= 1007 and 247 <= int(pos[1]) <= 313:
                    a = scorpius_init(player_pos, ALL_SPRITES=ALL_SPRITES)
                elif 1176 <= int(pos[0]) <= 1536 and 247 <= int(pos[1]) <= 313:
                    a = souleater_init(player_pos, ALL_SPRITES=ALL_SPRITES)
                elif 627 <= int(pos[0]) <= 1000 and 475 <= int(pos[1]) <= 548:
                    a = berserk_init(player_pos, ALL_SPRITES=ALL_SPRITES)
                if a:
                    start(player=a, ALL_SPRITES=ALL_SPRITES)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    stroka = input()
                    a = False
                    player_pos = pygame.Vector2(960, 520)
                    if stroka == 'general':
                        a = general_init(player_pos, ALL_SPRITES=ALL_SPRITES)
                    if stroka == 'negor':
                        a = egor_init(player_pos, ALL_SPRITES=ALL_SPRITES)
                    if a:
                        start(player=a, ALL_SPRITES=ALL_SPRITES)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
