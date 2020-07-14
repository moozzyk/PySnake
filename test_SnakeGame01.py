import unittest
from SnakeGame import SnakeGame, DOWN


class TestSnakeGame01(unittest.TestCase):
    def test_init_mandatory_paramaters(self):
        """
        Look at the __init__ method in the SnakeGame.py file. The method has width and
        height parameters. You need to use these parameters to initialize corresponding
        class variables. You can do it like this:
        self.width = width
        (You can ignore the `self` parameter)
        """
        game = SnakeGame(10, 15)
        self.assertEqual(game.width, 10)
        self.assertEqual(game.height, 15)

    def test_init_optional_parameters(self):
        """
        Look at the __init__ method int SnakeGame.py. file. The method has 3 parameters
        (food, snake, direction) that have assigned default values. The default values
        will be used if no values were provided for these parameters - like in the test
        above. Initialize corresponding class variables using these parameters. Don't worry
        about values for now.
        """
        game = SnakeGame(10, 15, food=[(5, 2)], snake=[(4, 6)], direction=DOWN)
        self.assertEqual([(5, 2)], game.food)
        self.assertEqual([(4, 6)], game.snake)
        self.assertEqual(DOWN, game.direction)

    def test_initial_snake_position(self):
        """
        The snake will be defined as a list of coordindates. Each coordinate will describe
        a position of a snake segment with the first item being the position of he head.
        The coordinate are in the form of (x, y) where (0, 0) is the top, left corner of the
        screen. For instance [(4, 6)] tells that the snake has only one segment (the head)
        which is located in the 4th column on the 6th row. When starting the game the snake
        should only have one segment (the head) positioned in the middle of the screen unless
        it was provided as the parameter to the __init__ method. Note we are going to use only
        integer coordinates (i.e. check different division operators)
        References:
         - lists: https://docs.python.org/3/tutorial/introduction.html#lists
         - numbers: https://docs.python.org/3/tutorial/introduction.html#numbers
        """
        game = SnakeGame(10, 15)
        self.assertEqual([(5, 7)], game.snake)


if __name__ == '__main__':
    unittest.main()
