import random
import pygame

from data import lobby
from data.anime import load_image
from data.mob_init import *

PIXEL = (20, 20)  # размеры стенок


def generate_lvl(name, screen, n, ALL_SPRITES):  # отрисовка уровней
    x = y = 0
    s = []
    if n == 2:
        wall = random.choice(['lvl2_field_wall.png', 'lvl2_forest_wall.png'])  # выбор стены для ур.2
    for row in name:
        for col in row:
            if col == "-":  # добавление стены в зависимости от уровня
                if n == 1:
                    from data.classes import Border
                    a = Border(x, y, 'lvl1_wall.png', ALL_SPRITES)
                elif n == 3:
                    from data.classes import Border
                    a = Border(x, y, 'lvl3_wall.png', ALL_SPRITES)
                else:
                    from data.classes import Border
                    a = Border(x, y, wall, ALL_SPRITES)
            else:
                s.append([x, y])  # пустая клетка (там может появиться моб)
                background = pygame.Surface(PIXEL)
                background.fill((0, 0, 0))
                screen.blit(background, (x, y))
            x += PIXEL[0]
        y += PIXEL[1]
        x = 0
        pygame.display.update()
        pygame.display.flip()
    return s  # возвращаем список пустых клеток


def generate_mobs(ALL_SPRITES, lvl_nomer, s, difficulty_nomer, room):  # появление мобов
    spisok = []
    for i in range(7):  # всего 7, т.к в комнате максимум 7 мобов
        pos = random.choice(s)  # выбор случайной пустой клетки для игрока
        while pos[0] >= 1920 - 128 or pos[1] >= 1080 - 128:
            pos = random.choice(s)
        pos = tuple(pos)
        mob = None
        boss = False
        if difficulty_nomer == 1 and room % 5 > 1:  # для ур. сложности легко:
            if lvl_nomer == 1:  # для ур.1
                a = random.randrange(0, 3)  # выбор типа моба
                if a == 0:
                    mob = archer_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = swordman_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = tank_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
            if lvl_nomer == 2:  # для ур.2
                a = random.randrange(0, 3)
                if a == 0:
                    mob = archer_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = swordman_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = tank_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
            if lvl_nomer == 3:  # для ур.3
                a = random.randrange(0, 3)
                if a == 0:
                    mob = archer_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = swordman_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = tank_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
        elif difficulty_nomer >= 2 and room % 5 > 1:  # для ур. сложности средне и сложно:
            if lvl_nomer == 1:  # для ур.1
                a = random.randrange(0, 3)  # выбор типа моба
                if a == 0:
                    mob = elite_archer_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = elite_swordman_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = elite_tank_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
            if lvl_nomer == 2:  # для ур.2
                a = random.randrange(0, 3)
                if a == 0:
                    mob = elite_archer_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = elite_swordman_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = elite_tank_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
            if lvl_nomer == 3:  # для ур.3
                a = random.randrange(0, 3)
                if a == 0:
                    mob = elite_archer_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = elite_swordman_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = elite_tank_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
        elif room % 5 == 0:  # генерация боссов
            if lvl_nomer == 1:  # босс ур.1
                mob = boss_lvl1_init(1, pos, ALL_SPRITES)
                boss = True
            if lvl_nomer == 2:  # босс ур.2
                a = random.randrange(0, 2)
                if a == 0:
                    mob = boss_lvl2_init_2(1, pos, ALL_SPRITES)
                if a == 1:
                    mob = boss_lvl2_init_1(1, pos, ALL_SPRITES)
                boss = True
            if lvl_nomer == 3:  # босс ур.3
                a = random.randrange(0, 3)
                mob = boss_lvl3_init(1, pos, ALL_SPRITES)
                boss = True
        if mob and not boss:  # если не босс
            spisok.append(mob)
        if boss:  # проверка на пень-колоду (там mob - кортеж, а нам нужны мобы из кортежа)
            if type(mob) == tuple:
                for r in mob:
                    spisok.append(r)
            else:
                spisok.append(mob)
            break
    return spisok  # возвращаем список мобов


def bad_ending():  # YOU DIED
    sound = 'sounds/'
    pygame.init()  # Инициация PyGame
    size = (1920, 1080)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Until it Done")
    image = load_image('died.jpg')
    clock = pygame.time.Clock()
    fps = 120
    sound1 = pygame.mixer.Sound(sound + 'died.mp3')
    channel = sound1.play()
    sound1.set_volume(1)
    screen.fill((0, 0, 0))
    running = True
    screen.blit(image, (1, 1))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # чтобы закрыть окно щелкаем по окну
                running = False
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)
        pygame.display.flip()
    sound1.stop()
    pygame.quit()
    lobby.lobby()


def good_ending():
    sound = 'sounds/'
    pygame.init()  # Инициация PyGame
    size = (1920, 1080)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Until it Done")
    image = load_image('win.png')
    clock = pygame.time.Clock()
    fps = 120
    sound1 = pygame.mixer.Sound(sound + 'Undertale.mp3')
    channel = sound1.play(-1)  # знач. -1 циклит мелодию
    sound1.set_volume(1)
    screen.fill((0, 0, 0))
    running = True
    screen.blit(image, (1, 1))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # выход по клику по окну
                running = False
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)
        pygame.display.flip()
    sound1.stop()
    pygame.quit()
    lobby.lobby()
