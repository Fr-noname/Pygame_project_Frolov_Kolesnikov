from data import game
from data.anime import *


def lobby(difficulty_nomer=1):
    sound = 'sounds/'
    pygame.init()
    image = load_image('lobby.png')
    size = w, h = (1920, 1080)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 144
    running = True
    screen.blit(image, (1, 1))
    sound1 = pygame.mixer.Sound(sound + 'Undertale.mp3')
    channel = sound1.play(-1)
    sound1.set_volume(1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if 50 <= int(pos[0]) <= 1025:
                    if 400 <= int(pos[1]) <= 475:
                        game.choose_of_character(difficulty_nomer=difficulty_nomer)
                    elif 525 <= int(pos[1]) <= 600:
                        game.setings()
                    elif 650 <= int(pos[1]) <= 725:
                        running = False
        pygame.display.flip()
        # print(clock.get_fps())
        clock.tick(fps)

    pygame.quit()
