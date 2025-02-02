import pygame
import sys

from data import characters
from data import lobby
from data.anime import *
from levels.lvls import *
from data.characters_init import *
from data.mob_init import *


def start(difficulty_nomer=1, room=1, lvl_nomer=1, player=None, ALL_SPRITES=None, kills=0):  # Сама игра
    sound = 'sounds/'
    pygame.init()  # Инициация PyGame
    flag = False
    size = (1920, 1080)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Until it Done")  # Даем название окну
    clock = pygame.time.Clock()
    fps = 120
    screen.fill((0, 0, 0))

    sound1 = pygame.mixer.Sound(sound + 'unknown_mystery_of_the_forest.mp3')
    channel = sound1.play(-1)
    sound1.set_volume(1)

    running = True

    if room != 1:  # Создание персонажа
        if type(player) == General:
            player = general_init(player, ALL_SPRITES)
        elif type(player) == SoulEater:
            player = souleater_init(player, ALL_SPRITES)
        elif type(player) == Scorpius:
            player = scorpius_init(player, ALL_SPRITES)
        elif type(player) == Paladin:
            player = paladin_init(player, ALL_SPRITES)
        elif type(player) == Berserk:
            player = berserk_init(player, ALL_SPRITES)
        elif type(player) == Egor:
            player = egor_init(player, ALL_SPRITES)

    s, mobs = lvl(lvl_nomer, screen, room, ALL_SPRITES, kills, lvl_nomer, difficulty_nomer)  # Генерация уровня и мобов

    player.x = 960  # Начальная позиция игрока
    player.y = 540

    pygame.draw.rect(screen, 'red', (21, 21, 10, player.hp), 0)  # Хп и щит (нее работает)
    pygame.draw.rect(screen, 'gray', (21, 31, 10, player.shield), 0)
    b_e = False

    while running:
        screen.fill("0x000000")
        for r in s:  # Отрисовка уровня
            b = pygame.Surface((20, 20))
            b.fill((0, 0, 0))
            screen.blit(b, r)
        pygame.draw.rect(screen, 'red', (1, 1, 10, player.hp), 0)  # отрисовка хп и щита (не работает)
        pygame.draw.rect(screen, 'gray', (1, 11, 10, player.shield), 0)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:  # ближняя атака
                    player.attack(mobs, ALL_SPRITES=ALL_SPRITES, w=0)
                if e.button == 3:  # дальняя атака
                    player.attack(mobs, ALL_SPRITES=ALL_SPRITES, w=1)

        for r in mobs:  # смерть моба
            if r.hp <= 0:
                r.kill()
                mobs = list(mobs)
                mobs.remove(r)
                kills += 1

        if player.hp <= 0:  # смерть игрока
            player.kill()
            running = False
            b_e = True

        player.movement()  # передвижение игрока
        for mob_test in mobs:  # передвижение мобов
            if mob_test.hp > 0:
                mob_test.movemnt(player.return_pos())

        ALL_SPRITES.draw(screen)  # Отрисовка спрайтов
        ALL_SPRITES.update()

        for mob_test in mobs:  # атака моба
            if mob_test.hp > 0:
                mob_test.damaging(player, ALL_SPRITES=ALL_SPRITES)

        pos = player.return_pos()
        if int(pos[0]) <= -50 or int(pos[0]) >= 1920 or int(pos[1]) <= -50 or int(pos[1]) >= 1080:  # переход
            # в следующую комнату
            room += 1
            flag = True
            running = False

        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
    for r in KLETKA:  # обнуление группы клетка
        r.kill()
    if flag:  # если перешли на следующий уровнь
        true_flag = True
        for r in ALL_SPRITES:  # обнуление мобов и игрока
            r.kill()

        if room % 5 == 0 and kills // 21 >= 1:  # Изменяем уровень
            lvl_nomer += 1
            kills = 0
            true_flag = True

        if room % 5 == 1 and lvl_nomer == 4:  # Хорошая концовка
            good_ending()
            true_flag = False

        if true_flag:  # Если не концовка
            start(room=room, lvl_nomer=lvl_nomer, player=player, ALL_SPRITES=ALL_SPRITES, kills=kills)
    if b_e:  # YOU DIED
        bad_ending()
    sys.exit()


def setings():  # Выбор уровня сложности
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
                    if 400 <= int(pos[1]) <= 475:  # уровень сложности: легко
                        difficulty_nomer = 1
                        running = False
                    elif 525 <= int(pos[1]) <= 600:  # уровень сложности: средне
                        difficulty_nomer = 2
                        running = False
                    elif 650 <= int(pos[1]) <= 725:  # уровень сложности: сложно
                        difficulty_nomer = 3
                        running = False
        screen.blit(image, (1, 1))
        pygame.display.flip()
    pygame.quit()
    lobby.lobby(difficulty_nomer=difficulty_nomer)  # Снова вызываем лобби


def choose_of_character(difficulty_nomer=1):  # выбор персонажа
    sound = 'sounds/'
    pygame.init()  # Инициация PyGame
    size = (1920, 1080)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Until it Done")
    image = load_image('characters.png')
    clock = pygame.time.Clock()
    fps = 120
    sound1 = pygame.mixer.Sound(sound + 'Undertale.mp3')
    channel = sound1.play(-1)
    sound1.set_volume(1)
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
                if 64 <= int(pos[0]) <= 457 and 247 <= int(pos[1]) <= 313:  # выбор паладина
                    a = paladin_init(player_pos, ALL_SPRITES=ALL_SPRITES)
                elif 619 <= int(pos[0]) <= 1007 and 247 <= int(pos[1]) <= 313:  # выбор скорпиуса
                    a = scorpius_init(player_pos, ALL_SPRITES=ALL_SPRITES)
                elif 1176 <= int(pos[0]) <= 1536 and 247 <= int(pos[1]) <= 313:  # выбор пожир. душ :D
                    a = souleater_init(player_pos, ALL_SPRITES=ALL_SPRITES)
                elif 627 <= int(pos[0]) <= 1000 and 475 <= int(pos[1]) <= 548:  # выбор берсерка
                    a = berserk_init(player_pos, ALL_SPRITES=ALL_SPRITES)
                if a:
                    start(player=a, ALL_SPRITES=ALL_SPRITES)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:  # выбор секретного персонажа
                    stroka = input()
                    a = False
                    player_pos = pygame.Vector2(960, 520)
                    if stroka == 'general':
                        a = general_init(player_pos, ALL_SPRITES=ALL_SPRITES)  # выбор генерала
                    if stroka == 'nEgor':
                        a = egor_init(player_pos, ALL_SPRITES=ALL_SPRITES)  # выбор прсонажа нЕгор
                    if a:
                        start(difficulty_nomer=difficulty_nomer, player=a, ALL_SPRITES=ALL_SPRITES)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)
        pygame.display.flip()
        sound1.stop()
        sound1.stop()
    pygame.quit()
