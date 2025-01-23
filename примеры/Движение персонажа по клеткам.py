import pygame
from collections import deque  # нужен чтобы быстро добавлять или удалять элементы
import time


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]

    def draw(self, surface):
        for x in range(self.width + 1):
            pygame.draw.line(surface, (255, 255, 255), (x * 40, 0), (x * 40, self.height * 40))
        for y in range(self.height + 1):
            pygame.draw.line(surface, (255, 255, 255), (0, y * 40), (self.width * 40, y * 40))
        for y in range(self.height):
            for x in range(self.width):
                color = (0, 0, 0)
                if self.board[y][x] == 1:
                    color = (0, 0, 255)
                elif self.board[y][x] == 2:
                    color = (255, 0, 0)
                pygame.draw.circle(surface, color, (x * 40 + 20, y * 40 + 20), 18)


class Lines(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.red_ball_pos = None
        self.path = None
        self.path_index = 0
        self.moving = False
        self.current_move_pos = None

    def find_path(self, x1, y1, x2, y2):
        if self.board[y1][x1] != 2 or self.board[y2][x2] != 0:
            return None
        visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        parent = [[None for _ in range(self.width)] for _ in range(self.height)]
        queue = deque([(x1, y1)])
        visited[y1][x1] = True

        while queue:  # это для проверки ан существование
            x, y = queue.popleft()  # удаление слева
            if (x, y) == (x2, y2):
                path = []
                while (x, y) is not None:
                    path.append((x, y))
                    if parent[y][x] is None:
                        break
                    x, y = parent[y][x]
                return path[::-1]

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and not visited[ny][nx]:
                    if self.board[ny][nx] == 0:
                        visited[ny][nx] = True
                        parent[ny][nx] = (x, y)
                        queue.append((nx, ny))
        return None

    def click(self, x, y):
        if self.board[y][x] == 0:
            if self.red_ball_pos:
                self.path = self.find_path(self.red_ball_pos[0], self.red_ball_pos[1], x, y)
                if self.path:
                    self.moving = True
                    self.path_index = 0
                    self.current_move_pos = self.red_ball_pos
            else:
                self.board[y][x] = 1
        elif self.board[y][x] == 1:
            self.board[y][x] = 2
            self.red_ball_pos = (x, y)
        elif self.board[y][x] == 2:
            self.board[y][x] = 1
            self.red_ball_pos = (x, y)

    def draw(self, surface):
        super().draw(surface)
        if self.moving and self.current_move_pos:
            x, y = self.current_move_pos
            pygame.draw.circle(surface, (255, 0, 0), (x * 40 + 20, y * 40 + 20), 18)

    def move_ball_step(self):
        if self.moving and self.path:
            if self.path_index < len(self.path):

                if self.path_index > 0:
                    prev_x, prev_y = self.path[self.path_index - 1]
                    self.board[prev_y][prev_x] = 0
                x, y = self.path[self.path_index]
                self.current_move_pos = (x, y)

                self.board[y][x] = 1
                self.path_index += 1
                time.sleep(0.1)
            else:
                self.moving = False
                if self.path:
                    last_x, last_y = self.path[-1]
                    self.board[last_y][last_x] = 1
                    self.board[self.path[0][1]][self.path[0][0]] = 0
                    self.path = None
                    self.current_move_pos = None
                    self.red_ball_pos = None


def main():
    pygame.init()
    width, height = 10, 10
    screen_size = 400
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Lines Game")
    clock = pygame.time.Clock()
    game = Lines(width, height)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                x, y = mouse_x // 40, mouse_y // 40
                if 0 <= x < width and 0 <= y < height:
                    game.click(x, y)
        if game.moving:
            game.move_ball_step()

        screen.fill((0, 0, 0))
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
