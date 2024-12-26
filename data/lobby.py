
from data import functions
import threading
import pygame
from data import game



def lobby():
    pygame.init()
    image = functions.load_image('lobby.png')
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
                        game.start(setings=[0])
                    elif 525 <= int(pos[1]) <= 600:
                        game.setings()
                    elif 650 <= int(pos[1]) <= 725:
                        running = False
        screen.blit(image, (1, 1))
        pygame.display.flip()


    pygame.quit()


