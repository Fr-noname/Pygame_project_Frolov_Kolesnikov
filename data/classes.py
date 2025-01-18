from data.anime import *
from data.functions import *

KLETKA = pygame.sprite.Group()


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, w, h):
        self.dx = 0
        self.dy = 0
        self.w = w
        self.h = h

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self.w // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - self.h // 2)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, ALL_SPRITES):
        super().__init__(ALL_SPRITES)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width // columns, sheet.get_height // rows)
        for r in range(rows):
            for t in range(columns):
                frame_location = (self.rect.x * r, self.rect.y * t)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Border(pygame.sprite.Sprite):
    def __init__(self, x, y, image_name, ALL_SPRITES):
        super().__init__(ALL_SPRITES)
        self.add(KLETKA)
        self.image = load_image(image_name)
        self.rect = pygame.Rect(x, y, 20, 20)
