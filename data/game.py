from pygame import QUIT

from data import characters
from data import lobby
from data.anime import *
from levels.lvls import *


def start(setings=1, room=1, lvl_nomer=1):
    pygame.init()  # Инициация PyGame
    kills = 30
    flag = False
    ALL_SPRITES = pygame.sprite.Group()
    size = (1920, 1080)
    player_pos = pygame.Vector2(size[0] // 2, size[1] // 2)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Until it Done")
    clock = pygame.time.Clock()
    fps = 120
    screen.fill((0, 0, 0))

    a = characters.Player(100, 100, 1, 1, 5, None,
                          None, None, player_pos, 'BLOB.png', ALL_SPRITES)
    running = True

    s = lvl(lvl_nomer, screen, room, ALL_SPRITES, kills)

    while running:
        screen.fill("0x000000")
        for r in s:
            b = pygame.Surface((20, 20))
            b.fill((0, 0, 0))
            screen.blit(b, r)

        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                a.attack()

        a.movement()

        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update()

        pos = a.return_pos()
        if int(pos[0]) <= -50 or int(pos[0]) >= 1920 or int(pos[1]) <= -50 or int(pos[1]) >= 1080:
            room += 1
            flag = True
            running = False

        pygame.display.update()
        pygame.display.flip()
        print(clock.get_fps())
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
    if flag:
        for r in ALL_SPRITES:
            r.kill()

        if room % 5 == 1 and kills // 30 >= 1:
            lvl_nomer += 1

        start(room=room, lvl_nomer=lvl_nomer)


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
