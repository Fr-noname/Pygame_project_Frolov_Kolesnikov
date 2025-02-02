from data import game
from data.anime import *


def lobby(difficulty_nomer=1):  # Функция лобби, повторяющиеся комменты не буду добавлять
    # (Например: Изображение загружаем)
    sound = 'sounds/'
    pygame.init()
    image = load_image('lobby.png')  # Изображение загружаем
    size = w, h = (1920, 1080)
    screen = pygame.display.set_mode(size)  # Создаем окно
    clock = pygame.time.Clock()
    fps = 144  # fps
    running = True
    screen.blit(image, (1, 1))
    sound1 = pygame.mixer.Sound(sound + 'Undertale.mp3')  # Звук на фоне
    channel = sound1.play(-1)
    sound1.set_volume(1)  # Громкость звука

    while running:  # Цикл игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # кнопки меню
                pos = event.pos
                if 50 <= int(pos[0]) <= 1025:
                    if 400 <= int(pos[1]) <= 475:  # кнопка выбора персонажа
                        game.choose_of_character(difficulty_nomer=difficulty_nomer)
                    elif 525 <= int(pos[1]) <= 600:  # Настройка уровня сложности
                        game.setings()
                    elif 650 <= int(pos[1]) <= 725:  # Выход из игры
                        running = False
        pygame.display.flip()
        # print(clock.get_fps())
        clock.tick(fps)

    pygame.quit()
