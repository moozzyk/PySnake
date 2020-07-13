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
        above. Initialize corresponding class variables using these parameters.
        """
        game = SnakeGame(10, 15, food=[], snake=[], direction=DOWN)
        self.assertEqual([], game.food)
        self.assertEqual([], game.snake)
        self.assertEqual(DOWN, game.direction)


if __name__ == '__main__':
    unittest.main()
