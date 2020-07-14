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
        """Object initialization logic"""
        self.width = width
        self.height = height
        self.food = food
        self.snake = snake or [(width // 2, height // 2)]
        self.direction = direction

    def move_snake(self):
        x, y = self.snake[0]
        if self.direction == UP:
            y -= 1
        if self.direction == DOWN:
            y += 1
        if self.direction == LEFT:
            x -= 1
        if self.direction == RIGHT:
            x += 1

        self.snake = [(x, y)]
