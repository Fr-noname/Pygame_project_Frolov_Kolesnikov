import pygame
from data import lobby

if __name__ == "__main__":
    lobby.lobby()


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
