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
        self.status = PLAYING

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
            self.add_food_if_needed()
        else:
            self.snake = [(x, y)] + self.snake[0: -1]

    def snake_is_alive(self):
        head_x, head_y = self.snake[0]
        return head_x >= 0 and head_x < self.width and head_y >= 0 and head_y < self.height and self.snake[0] not in self.snake[1:]

    def tick(self):
        if self.status != PLAYING:
            return

        self.move_snake()

        if not self.snake_is_alive():
            self.status = GAME_OVER
        elif len(self.snake) == self.width * self.height:
            self.status = GAME_WON
