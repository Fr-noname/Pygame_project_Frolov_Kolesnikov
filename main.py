import pygame
from data import lobby

if __name__ == "__main__":
    lobby.lobby()



import pygame


class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.board = [[0] * w for r in range(h)]
        self.left = 10
        self.top = 10
        self.cell_s = 30
        self.mouse_pos = tuple()
        self.screen = 0

    def render(self, screen):
        self.screen = screen
        for r in range(self.w):
            for i in range(self.h):
                pygame.draw.rect(screen, (0, 0, 0), (r * self.cell_s + self.left,
                                                           i * self.cell_s + self.top, self.cell_s, self.cell_s)
                                 , self.board[i][r])

    def set_view(self, le, top, cell_s):
        self.left = le
        self.top = top
        self.cell_s = cell_s

    def get_click(self, mouse_pos):
        self.mouse_pos = mouse_pos
        cell = self.get_cell(self.mouse_pos)
        self.on_click(tuple(cell))

    def get_cell(self, mouse_pos):
        x = (self.mouse_pos[0] - self.left) // self.cell_s
        y = (self.mouse_pos[1] - self.top) // self.cell_s
        if 0 <= x + 1 <= self.w and 0 <= y + 1 <= self.h:
            return x, y

    def on_click(self, t):
        x, y = t
        self.board[y][x] = int(not self.board[y][x])
        self.render(self.screen)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
board = Board(12, 7)
board.set_view(0, 0, 100)
running = True
dt = 20
v = 20
fps = 60


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= v * dt
    if keys[pygame.K_s]:
        player_pos.y += v * dt
    if keys[pygame.K_a]:
        player_pos.x -= v * dt
    if keys[pygame.K_d]:
        player_pos.x += v * dt
    screen.fill("white")
    board.render(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(fps) / 1000

pygame.quit()
