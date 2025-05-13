# Created by Joe Habre
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.SysFont("arial", 24)
big_font = pygame.font.SysFont("arial", 48)

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

clock = pygame.time.Clock()

def draw_snake(snake_blocks):
    for block in snake_blocks:
        pygame.draw.rect(screen, GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

def draw_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def message(text, size, color, y_offset=0):
    if size == "small":
        msg = font.render(text, True, color)
    else:
        msg = big_font.render(text, True, color)
    rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(msg, rect)

def game_loop():
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    snake = [(x, y)]
    direction = "RIGHT"
    score = 0

    food = (
        random.randrange(0, WIDTH, BLOCK_SIZE),
        random.randrange(0, HEIGHT, BLOCK_SIZE)
    )

    running = True
    while running:
        clock.tick(FPS + score // 3)
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_w] and direction != "DOWN":
                    dx, dy = 0, -BLOCK_SIZE
                    direction = "UP"
                elif event.key in [pygame.K_DOWN, pygame.K_s] and direction != "UP":
                    dx, dy = 0, BLOCK_SIZE
                    direction = "DOWN"
                elif event.key in [pygame.K_LEFT, pygame.K_a] and direction != "RIGHT":
                    dx, dy = -BLOCK_SIZE, 0
                    direction = "LEFT"
                elif event.key in [pygame.K_RIGHT, pygame.K_d] and direction != "LEFT":
                    dx, dy = BLOCK_SIZE, 0
                    direction = "RIGHT"

        # Move snake
        x += dx
        y += dy
        head = (x, y)
        snake.insert(0, head)

        # Check collisions
        if (
            x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or
            head in snake[1:]
        ):
            screen.fill(BLACK)
            message("Game Over!", "big", RED)
            message("Press R to Restart or Q to Quit", "small", WHITE, 50)
            pygame.display.update()

            while True:
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_loop()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

        # Check if food is eaten
        if head == food:
            score += 1
            food = (
                random.randrange(0, WIDTH, BLOCK_SIZE),
                random.randrange(0, HEIGHT, BLOCK_SIZE)
            )
        else:
            snake.pop()

        draw_food(food)
        draw_snake(snake)
        draw_score(score)

        pygame.display.update()

game_loop()

