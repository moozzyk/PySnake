import pygame
import time
from SnakeGame import SnakeGame, UP, DOWN, LEFT, RIGHT, PLAYING, GAME_OVER

WIDTH = 50
HEIGHT = 40
FIELD_SIZE = 12

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (127, 0, 0)
BROWN = (121, 63, 13)
GREEN = (0, 147, 0)

WALL_COLOR = RED
SNAKE_COLOR = BROWN
FOOD_COLOR = GREEN


def draw_walls(display):
    pygame.draw.rect(
        display, WALL_COLOR, (0, 0, (2 + WIDTH) * FIELD_SIZE, FIELD_SIZE))
    pygame.draw.rect(
        display, WALL_COLOR, (0, (1 + HEIGHT) * FIELD_SIZE, (2 + WIDTH) * FIELD_SIZE, FIELD_SIZE))
    pygame.draw.rect(
        display, WALL_COLOR, (0, FIELD_SIZE, FIELD_SIZE, HEIGHT * FIELD_SIZE))
    pygame.draw.rect(
        display, WALL_COLOR, ((1 + WIDTH) * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE, HEIGHT * FIELD_SIZE))


def draw_snake(display, game):
    for (x, y) in game.snake:
        pygame.draw.rect(display, SNAKE_COLOR, ((
            1 + x) * FIELD_SIZE, (1 + y) * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))


def draw_food(display, game):
    for (x, y) in game.food:
        pygame.draw.rect(display, FOOD_COLOR, ((
            1 + x) * FIELD_SIZE, (1 + y) * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))


def draw_arena(display, game):
    display.fill(WHITE)
    draw_walls(display)
    draw_food(display, game)
    draw_snake(display, game)


def main():
    game = SnakeGame(width=WIDTH, height=HEIGHT)
    pygame.init()
    display = pygame.display.set_mode(
        ((2 + WIDTH) * FIELD_SIZE, (2 + HEIGHT) * FIELD_SIZE))
    pygame.display.set_caption('PySnake')
    display.fill(WHITE)

    last_time = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.change_direction(UP)
                if event.key == pygame.K_DOWN:
                    game.change_direction(DOWN)
                if event.key == pygame.K_LEFT:
                    game.change_direction(LEFT)
                if event.key == pygame.K_RIGHT:
                    game.change_direction(RIGHT)

        current_time = time.time() * 1000
        if game.status == PLAYING and current_time - last_time > 100:
            last_time = current_time
            game.tick()
            draw_arena(display, game)
            pygame.display.update()


if __name__ == '__main__':
    main()
