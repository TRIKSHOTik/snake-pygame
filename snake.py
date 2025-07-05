import pygame

pygame.init()

CELL_SIZE = 30
desktop_size = pygame.display.get_desktop_sizes()[0]
WIDTH, HEIGHT = desktop_size[0] // 2, desktop_size[1] // 1.5
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Snake:
    def __init__(self, start_body=None):
        if start_body is None:
            start_body = [(300, 300), (320, 300)]
        self.body = start_body
        self.head_skin = None
        self.direction = (20, 0)

    def move(self):
        head_pos = self.body[0]
        new_head_pos = (head_pos[0] + self.direction[0], head_pos[1] + self.direction[1])
        self.body.insert(0, new_head_pos)
        self.body.pop()

    def draw_snake(self):
        for body in self.body:
            pygame.draw.rect(screen, pygame.Color('black'), [body[0], body[1], CELL_SIZE, CELL_SIZE])

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def change_direction(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.direction = (0, -20)
            elif event.key == pygame.K_DOWN:
                self.direction = (0, 20)
            elif event.key == pygame.K_LEFT:
                self.direction = (-20, 0)
            elif event.key == pygame.K_RIGHT:
                self.direction = (20, 0)

    def collide(self, screen_sizes):
        if not (0 <= self.body[0][0] <= screen_sizes[0] and 0 <= self.body[0][1] <= screen_sizes[1]):
            return True
        if self.body[0][0] in self.body[1:]:
            return True
        return False