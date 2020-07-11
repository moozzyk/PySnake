UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class SnakeEngine:
    def __init__(self, width, height, food=[], snake=None, direction=UP):
        # TODO: validate width, height
        self.witdh = width
        self.height = height
        self.food = food
        self.snake = snake or [(width / 2, height / 2)]
        self.direction = direction

    def change_direction(self, new_direction):
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

        self.snake = [(x, y)] + self.snake[:-1]

    def tick(self):
        self.move_snake()
