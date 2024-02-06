import pygame
import random

#Atur jendela game
pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

#variable permainan
snake_size = 20
snake_speed = 15

font = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()

#fungsi untuk menampilkan skor
def show_score(score):
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

#fungsi untuk menggambar ular
def draw_snake(snake_body):
    for body_part in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), (body_part[0], body_part[1], snake_size, snake_size))

#loop utama permainan untuk menangani input pemain, pergerakan ular, dan kondisi permainan
def game_loop():
    game_over = False
    game_quit = False

    # Inisialisasi posisi awal ular
    x = width // 2
    y = height // 2

    x_change = 0
    y_change = 0

    snake_body = []
    snake_length = 1

    # Inisialisasi posisi makanan
    food_x = round(random.randrange(0, width - snake_size) / 20) * 20
    food_y = round(random.randrange(0, height - snake_size) / 20) * 20

    while not game_quit:
        while game_over:
            screen.fill((0, 0, 0))
            game_over_text = font.render("Game Over! Press C-Play Again or Q-Quit", True, (255, 255, 255))
            screen.blit(game_over_text, (width // 2 - 200, height // 2 - 30))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0

        # Batasan jendela game
        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        # Mengubah posisi ular
        x += x_change
        y += y_change

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, snake_size, snake_size))

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        for body_part in snake_body[:-1]:
            if body_part == snake_head:
                game_over = True

        draw_snake(snake_body)
        show_score(snake_length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 20) * 20
            food_y = round(random.randrange(0, height - snake_size) / 20) * 20
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

