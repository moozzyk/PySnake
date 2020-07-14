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


if __name__ == '__main__':
    unittest.main()
