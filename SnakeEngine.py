UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


class SnakeEngine:
    def __init__(self, width, height, food=[], snake=None, direction=UP):
        # TODO: validate width, height
        self.witdh = width
        self.height = height
        self.food = food
        self.snake = snake or [(width / 2, height / 2)]
        self.direction = direction
