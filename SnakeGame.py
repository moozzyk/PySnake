from random import randint

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

PLAYING = 0
GAME_OVER = 1
GAME_WON = 2


class SnakeGame:
    def __init__(self, width, height, food=None, snake=None, direction=UP):
        self.width = width
        self.height = height
        self.food = food
        self.snake = snake or [(width // 2, height // 2)]
        self.direction = direction
