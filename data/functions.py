import random
import pygame

from data import lobby
from data.anime import load_image
from data.mob_init import *

PIXEL = (20, 20)


def generate_lvl(name, screen, n, ALL_SPRITES):
    x = y = 0
    s = []
    if n == 2:
        wall = random.choice(['lvl2_field_wall.png', 'lvl2_forest_wall.png'])
    for row in name:
        for col in row:
            if col == "-":
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
                s.append([x, y])
                background = pygame.Surface(PIXEL)
                background.fill((0, 0, 0))
                screen.blit(background, (x, y))
            x += PIXEL[0]
        y += PIXEL[1]
        x = 0
        pygame.display.update()
        pygame.display.flip()
    return s


def generate_mobs(ALL_SPRITES, lvl, s, difficulty_nomer, room):
    spisok = []
    print(s)
    for i in range(7):
        pos = random.choice(s)
        while pos[0] >= 1920 - 128 or pos[1] >= 1080 - 128:
            pos = random.choice(s)
        pos = tuple(pos)
        mob = None
        if difficulty_nomer == 1 and room % 5 > 1:
            if lvl == 1:
                a = random.randrange(0, 3)
                if a == 0:
                    mob = archer_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = swordman_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = tank_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
            if lvl == 2:
                a = random.randrange(0, 3)
                if a == 0:
                    mob = archer_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = swordman_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = tank_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
            if lvl == 3:
                a = random.randrange(0, 3)
                if a == 0:
                    mob = archer_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = swordman_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = tank_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
        elif difficulty_nomer >= 2 and room % 5 > 1:
            if lvl == 1:
                a = random.randrange(0, 3)
                if a == 0:
                    mob = elite_archer_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = elite_swordman_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = elite_tank_lvl1_init(1, pygame.Vector2(pos), ALL_SPRITES)
            if lvl == 2:
                a = random.randrange(0, 3)
                if a == 0:
                    mob = elite_archer_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = elite_swordman_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = elite_tank_lvl2_init(1, pygame.Vector2(pos), ALL_SPRITES)
            if lvl == 3:
                a = random.randrange(0, 3)
                if a == 0:
                    mob = elite_archer_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 1:
                    mob = elite_swordman_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
                if a == 2:
                    mob = elite_tank_lvl3_init(1, pygame.Vector2(pos), ALL_SPRITES)
        if mob:
            spisok.append(mob)
    return spisok


def bad_ending():
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)
        pygame.display.flip()
    sound1.stop()
    pygame.quit()
    lobby.lobby()


def game_win():
    pass


global DifficultyNomer
DifficultyNomer = 1

Pixel = (20, 20)
