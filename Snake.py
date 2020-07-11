import pygame
import time
from SnakeEngine import SnakeEngine, UP, DOWN, LEFT, RIGHT

WIDTH = 75
HEIGHT = 50
FIELD_SIZE = 10

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


def draw_snake(display, engine):
    for (x, y) in engine.snake:
        pygame.draw.rect(display, SNAKE_COLOR, ((
            1 + x) * FIELD_SIZE, (1 + y) * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))


def draw_food(display, engine):
    for (x, y) in engine.food:
        pygame.draw.rect(display, FOOD_COLOR, ((
            1 + x) * FIELD_SIZE, (1 + y) * FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))


def draw_arena(display, engine):
    display.fill(WHITE)
    draw_walls(display)
    draw_food(display, engine)
    draw_snake(display, engine)


def main():
    engine = SnakeEngine(width=WIDTH, height=HEIGHT)
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
                    engine.change_direction(UP)
                if event.key == pygame.K_DOWN:
                    engine.change_direction(DOWN)
                if event.key == pygame.K_LEFT:
                    engine.change_direction(LEFT)
                if event.key == pygame.K_RIGHT:
                    engine.change_direction(RIGHT)

        current_time = time.time() * 1000
        if current_time - last_time > 100:
            print(current_time)
            last_time = current_time
            engine.tick()
            draw_arena(display, engine)
            pygame.display.update()


if __name__ == '__main__':
    main()
