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
        # TODO: validate width, height
        self.width = width
        self.height = height
        self.food = food
        self.snake = snake or [(width // 2, height // 2)]
        self.food = food or []
        self.add_food_if_needed()
        self.direction = direction
        self.status = PLAYING

    def change_direction(self, new_direction):
        # TODO: validate direction
        if self.direction != (new_direction + 2) % 4:
            self.direction = new_direction

    def move_snake(self):
        (x, y) = self.snake[0]
        if self.direction == UP:
            y -= 1
        elif self.direction == RIGHT:
            x += 1
        elif self.direction == DOWN:
            y += 1
        elif self.direction == LEFT:
            x -= 1

        if self.try_eat_food():
            self.snake = [(x, y)] + self.snake
        else:
            self.snake = [(x, y)] + self.snake[:-1]

    def try_eat_food(self):
        head = self.snake[0]
        if head in self.food:
            self.food.remove(head)
            return True
        return False

    def add_food_if_needed(self):
        if len(self.food) > 0:
            return

        while True:
            food_position = (randint(0, self.width - 1),
                             randint(0, self.height - 1))
            if not(food_position in self.food or food_position in self.snake):
                self.food = self.food + [food_position]
                return

    def is_snake_alive(self):
        (head_x, head_y) = self.snake[0]
        if head_x < 0 or head_x == self.width or head_y < 0 or head_y == self.height:
            return False

        return not self.snake[0] in self.snake[1:]

    def tick(self):
        if self.status == GAME_OVER:
            return

        self.move_snake()
        if not self.is_snake_alive():
            self.status = GAME_OVER
            return

        self.add_food_if_needed()
