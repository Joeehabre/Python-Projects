# Created by Joe Habre
import pygame
import random
import sys
import json
import os

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK = 20
FPS_BASE = 8

BLACK      = (0,   0,   0)
DARK_GRAY  = (20,  20,  20)
GRID_COLOR = (30,  30,  30)
GREEN      = (0,  200,  0)
HEAD_COLOR = (0,  255, 80)
RED        = (220,  50,  50)
WHITE      = (255, 255, 255)
YELLOW     = (255, 220,  0)
ORANGE     = (255, 140,  0)

font_sm  = pygame.font.SysFont("arial", 20)
font_med = pygame.font.SysFont("arial", 28)
font_big = pygame.font.SysFont("arial", 52, bold=True)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

SCORES_FILE = os.path.join(os.path.dirname(__file__), "highscore.json")


def load_high_score():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE) as f:
                return json.load(f).get("high_score", 0)
        except Exception:
            pass
    return 0


def save_high_score(score):
    with open(SCORES_FILE, "w") as f:
        json.dump({"high_score": score}, f)


def draw_grid():
    for x in range(0, WIDTH, BLOCK):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))


def draw_snake(snake):
    for i, block in enumerate(snake):
        color = HEAD_COLOR if i == 0 else GREEN
        pygame.draw.rect(screen, color, (*block, BLOCK, BLOCK))
        pygame.draw.rect(screen, BLACK, (*block, BLOCK, BLOCK), 1)


def draw_food(food):
    pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))
    pygame.draw.rect(screen, ORANGE, (*food, BLOCK, BLOCK), 2)


def blit_center(surface, y_offset=0):
    rect = surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(surface, rect)


def spawn_food(snake_set):
    all_cells = {
        (x, y)
        for x in range(0, WIDTH, BLOCK)
        for y in range(0, HEIGHT, BLOCK)
    }
    free = list(all_cells - snake_set)
    return random.choice(free) if free else (0, 0)


def game_loop():
    high_score = load_high_score()

    while True:
        x, y = WIDTH // 2 - WIDTH // 2 % BLOCK, HEIGHT // 2 - HEIGHT // 2 % BLOCK
        dx, dy = BLOCK, 0
        direction = "RIGHT"
        next_direction = "RIGHT"
        snake = [(x, y)]
        snake_set = {(x, y)}
        score = 0
        paused = False

        food = spawn_food(snake_set)

        running = True
        while running:
            fps = FPS_BASE + score // 5
            clock.tick(fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save_high_score(high_score)
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = not paused

                    if not paused:
                        if event.key in (pygame.K_UP, pygame.K_w) and direction != "DOWN":
                            next_direction = "UP"
                        elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != "UP":
                            next_direction = "DOWN"
                        elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != "RIGHT":
                            next_direction = "LEFT"
                        elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != "LEFT":
                            next_direction = "RIGHT"

            if paused:
                screen.fill(DARK_GRAY)
                draw_grid()
                draw_food(food)
                draw_snake(snake)
                blit_center(font_big.render("PAUSED", True, YELLOW))
                blit_center(font_sm.render("Press P to resume", True, WHITE), 55)
                pygame.display.update()
                continue

            direction = next_direction
            if direction == "UP":    dx, dy = 0, -BLOCK
            elif direction == "DOWN":  dx, dy = 0,  BLOCK
            elif direction == "LEFT":  dx, dy = -BLOCK, 0
            elif direction == "RIGHT": dx, dy =  BLOCK, 0

            nx, ny = snake[0][0] + dx, snake[0][1] + dy
            head = (nx, ny)

            if nx < 0 or nx >= WIDTH or ny < 0 or ny >= HEIGHT or head in snake_set:
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)

                screen.fill(DARK_GRAY)
                blit_center(font_big.render("GAME OVER", True, RED), -60)
                blit_center(font_med.render(f"Score: {score}   Best: {high_score}", True, WHITE))
                blit_center(font_sm.render("R = Restart    Q = Quit", True, YELLOW), 55)
                pygame.display.update()

                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                waiting = False
                                running = False
                            elif event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()
                continue

            snake.insert(0, head)
            snake_set.add(head)

            if head == food:
                score += 1
                food = spawn_food(snake_set)
            else:
                tail = snake.pop()
                snake_set.discard(tail)

            screen.fill(DARK_GRAY)
            draw_grid()
            draw_food(food)
            draw_snake(snake)

            score_surf = font_sm.render(f"Score: {score}   Best: {high_score}   P=Pause", True, WHITE)
            screen.blit(score_surf, (10, 10))

            pygame.display.update()


game_loop()
