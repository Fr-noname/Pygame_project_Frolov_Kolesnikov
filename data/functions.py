import random
import pygame
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


global DifficultyNomer
DifficultyNomer = 1

Pixel = (20, 20)
