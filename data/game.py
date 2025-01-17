from pygame import QUIT

from data import characters
from data import lobby
from data.functions import *
from levels.rooms import *
from data.classes import *


def start(setings=1):
    pygame.init()  # Инициация PyGame
    size = (1920, 1080)
    player_pos = pygame.Vector2(size[0] // 2, size[1] // 2)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Until it Done")
    clock = pygame.time.Clock()
    fps = 120

    a = characters.Player(100, 100, 1, 1, 5, None, None, None, player_pos)
    running = True

    s = generate_lvl(battle_room4_r_v, screen)

    while running:
        screen.fill("0x000000")
        for r in s:
            b = Surface((20, 20))
            b.fill((255, 0, 255))
            screen.blit(b, r)

        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                a.attack()

        keys = pygame.key.get_pressed()

        a.movement()

        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update()

        pygame.display.update()
        pygame.display.flip()
        print(clock.get_fps())
        clock.tick(fps)
        pygame.display.flip()
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
