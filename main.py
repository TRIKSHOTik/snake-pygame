import pygame
import sys
import time
# from snake import Snake

pygame.init()

WIDTH, HEIGHT = 1600, 1600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Unleashed")
pygame.display.set_icon(pygame.image.load("img/logo.jpeg"))

snake_loading_image = pygame.image.load("img/snake_u.jpeg")
snake_loading_image = pygame.transform.scale(snake_loading_image, (WIDTH, HEIGHT))

main_snake_bg = pygame.image.load("img/main_snake.png")
main_snake_bg = pygame.transform.scale(main_snake_bg, (WIDTH, HEIGHT))

play_button_image = pygame.image.load("img/play.png")

font = pygame.font.SysFont("Arial", 40)
button_font = pygame.font.SysFont("Arial", 32)
clock = pygame.time.Clock()


def draw_button_with_image(image, x, y, w, h, action=None):
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

        loading_text = font.render(loading_phases[current_phase], True, (255, 255, 255))
        screen.blit(loading_text, (WIDTH // 2 - loading_text.get_width() // 2, HEIGHT - 80))

        pygame.display.update()
        clock.tick(60)


def main_menu():
    running = True
    while running:
        screen.blit(main_snake_bg, (0, 0))
        draw_button_with_image(play_button_image, WIDTH // 2 - 715 // 2, HEIGHT // 2, 715, 220)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

show_loading_screen()
main_menu()
