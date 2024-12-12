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

    def render(self, screen):
        for r in range(self.w):
            for i in range(self.h):
                pygame.draw.rect(screen, (255, 255, 255), (r * self.cell_s + self.left,
                                                           i * self.cell_s + self.top, self.cell_s, self.cell_s), 1)

    def set_view(self, le, top, cell_s):
        self.left = le
        self.top = top
        self.cell_s = cell_s



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()
board = Board(40, 24)
board.set_view(0, 0, 5)
running = True
dt = 0
v = 500
fps = 60


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= v * dt
    if keys[pygame.K_s]:
        player_pos.y += v * dt
    if keys[pygame.K_a]:
        player_pos.x -= v * dt
    if keys[pygame.K_d]:
        player_pos.x += v * dt
    screen.fill("black")
    board.render(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(fps) / 1000

pygame.quit()
