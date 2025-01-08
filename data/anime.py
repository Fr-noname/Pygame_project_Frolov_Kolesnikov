import random
import time

from data import functions


def lobby_anime(screen):
    screen = screen[0]
    im_1 = functions.load_image('lobby.png')
    im_2 = functions.load_image('lobby-1.png')
    im_3 = functions.load_image('lobby-2.png')
    screen.blit(im_1, (1, 1))
    a = random.randrange(1, 40)
    # time.sleep(a)
    for r in range(random.randrange(1, 10)):
        a = random.randrange(1, 5)
        b = random.randrange(1, 5)
        screen.blit(im_2, (1, 1))
        time.sleep(a)
        screen.blit(im_3, (1, 1))
        time.sleep(b)
    screen.blit(im_1, (1, 1))
