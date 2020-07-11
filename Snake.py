import pygame
from SnakeEngine import SnakeEngine

WIDTH = 75
HEIGHT = 50
FIELD_SIZE = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (127, 0, 0)


def draw_arena(display, engine):
    for row in range(engine.arena_height):
        for col in range(engine.arena_width):
            field = engine.get_field(row, col)
            if field == ' ':
                pygame.draw.rect(
                    display, RED, (col * FIELD_SIZE, row * FIELD_SIZE, FIELD_SIZE - 1, FIELD_SIZE - 1))


def main():
    pygame.init()
    display = pygame.display.set_mode(
        (WIDTH * FIELD_SIZE, HEIGHT * FIELD_SIZE))
    pygame.display.set_caption('PySnake')
    display.fill(WHITE)
    engine = SnakeEngine(width=WIDTH, height=HEIGHT)
    print(f'{engine.arena_width} {engine.arena_height}')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        draw_arena(display, engine)
        pygame.display.update()


if __name__ == '__main__':
    main()
