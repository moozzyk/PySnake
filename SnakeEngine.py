UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

PLAYING = 0
GAME_OVER = 1
GAME_WON = 2


class SnakeEngine:
    def __init__(self, width, height, food=[], snake=None, direction=UP):
        # TODO: validate width, height
        self.width = width
        self.height = height
        self.food = food
        self.snake = snake or [(width // 2, height // 2)]
        self.direction = direction
        self.status = PLAYING

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

    def is_snake_alive(self):
        (head_x, head_y) = self.snake[0]
        print(head_x)
        if head_x < 0 or head_x == self.width or head_y < 0 or head_y == self.height:
            return False

        for segment in self.snake[1:]:
            if segment == self.snake[0]:
                return False

        return True

    def tick(self):
        if self.status == GAME_OVER:
            return

        self.move_snake()
        if not self.is_snake_alive():
            self.status = GAME_OVER
            return
