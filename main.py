import pygame
import sys
import time
from snake import Snake
from field import Field

pygame.init()

CELL_SIZE = 30
desktop_size = pygame.display.get_desktop_sizes()[0]
WIDTH, HEIGHT = desktop_size[0] // 2, desktop_size[1] // 1.5
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake Unleashed")
pygame.display.set_icon(pygame.image.load("img/logo.jpeg"))
snake_loading_image = pygame.image.load("img/snake_u.jpeg")
snake_loading_image = pygame.transform.scale(snake_loading_image, (WIDTH, HEIGHT))
main_snake_bg = pygame.image.load("img/main_snake.png")
main_snake_bg = pygame.transform.scale(main_snake_bg, (WIDTH, HEIGHT))
play_button_image = pygame.image.load("img/play.png")
font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

running = False
waiting = True


def start_game():
    global waiting, running
    waiting = False
    running = True


def draw_button_with_image(image, x, y, w, h, action=start_game):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        hover_image = pygame.transform.scale(image, (int(w * 1.05), int(h * 1.05)))
        screen.blit(hover_image, (x - (hover_image.get_width() - w) // 2,
                                  y - (hover_image.get_height() - h) // 2))
        if click[0] == 1 and action:
            action()
    else:
        screen.blit(pygame.transform.scale(image, (w, h)), (x, y))


def show_loading_screen(duration=3):
    start_time = time.time()
    loading_phases = ["Loading", "Loading.", "Loading..", "Loading..."]
    current_phase = 0
    phase_timer = 0

    while time.time() - start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(snake_loading_image, (0, 0))

        phase_timer += clock.get_time()
        if phase_timer >= 500:
            phase_timer = 0
            current_phase = (current_phase + 1) % len(loading_phases)

        loading_text = font.render(loading_phases[current_phase], True, (253, 177, 3))
        screen.blit(loading_text, (WIDTH // 2 - loading_text.get_width() // 2, HEIGHT - 80))

        pygame.display.update()
        clock.tick(60)


def game_loop():
    global running
    snake = Snake()
    field = Field()
    food = field.generate_food(snake.body)
    score = 0

    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            snake.change_direction(event)

        snake.move()

        if snake.collide((WIDTH, HEIGHT)):
            running = False
            break

        if snake.body[0] == food:
            snake.grow()
            food = field.generate_food(snake.body)
            score += 1
        pygame.draw.rect(screen, pygame.Color('red'), (food[0], food[1], CELL_SIZE, CELL_SIZE))

        snake.draw_snake()

        pygame.display.flip()
        clock.tick(10)


def main_menu():
    global waiting
    show_loading_screen()
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(main_snake_bg, (0, 0))
        draw_button_with_image(play_button_image, WIDTH // 2 - 715 // 2, HEIGHT // 2, 715, 220)
        pygame.display.update()
    else:
        game_loop()

main_menu()