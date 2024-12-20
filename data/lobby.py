import os
import sys

import pygame



def lobby():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()
    im = load_image('creature.png', -1)
    running = True

    dt = 0

    player_pos = pygame.Vector2(1, 1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("white")

        screen.blit(im, player_pos)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_pos.y -= 10
        if keys[pygame.K_DOWN]:
            player_pos.y += 10
        if keys[pygame.K_LEFT]:
            player_pos.x -= 10
        if keys[pygame.K_RIGHT]:
            player_pos.x += 10
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()

def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()  # создаёт новую копию изображения с таким же форматом пикселей, как у экрана
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()  # метод для преобразования изображения с сохранением информации о прозрачности
    return image
