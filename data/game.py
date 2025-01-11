from pygame import QUIT

from data import characters
from data import lobby
from data.functions import *
from levels.rooms import *


def start(setings=1):
    pygame.init()  # Инициация PyGame
    im = load_image('LIFESTEALER.png', -1)
    player_pos = pygame.Vector2(1, 1)
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Until it Done")
    clock = pygame.time.Clock()
    fps = 120

    a = characters.Player(100, 100, 1, 1, 20, None, None, None)
    running = True

    room_show(battle_room3_l_n, screen, im, player_pos)

    while running:
        room_show(battle_room3_l_n, screen, im, player_pos)

        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                a.attack()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            player_pos.y -= a.get_information()[-1]
        if keys[pygame.K_s]:
            player_pos.y += a.get_information()[-1]
        if keys[pygame.K_a]:
            player_pos.x -= a.get_information()[-1]
        if keys[pygame.K_d]:
            player_pos.x += a.get_information()[-1]
        if keys[pygame.K_TAB]:
            a.change_weapon()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


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
