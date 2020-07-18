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
        self.food = food or []
        self.snake = snake or [(width // 2, height // 2)]
        self.direction = direction
        self.add_food_if_needed()

    def add_food_if_needed(self):
        if self.food or len(self.snake) == self.width * self.height:
            return

        while True:
            food_position = (randint(0, self.width - 1),
                             randint(0, self.height - 1))
            if not food_position in self.snake:
                self.food = [food_position]
                return

    def change_direction(self, new_direction):
        if self.direction != (new_direction + 2) % 4:
            self.direction = new_direction

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

        if self.food[0] == (x, y):
            self.snake = [(x, y)] + self.snake
            self.food = []
        else:
            self.snake = [(x, y)] + self.snake[0: -1]

    def tick(self):
        self.move_snake()
