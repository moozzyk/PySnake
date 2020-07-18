import unittest
from SnakeGame import SnakeGame, LEFT

"""
After you make these tests pass and run the game you will be able to eat
the food and grow the snake.
"""


class TestSnakeGame04(unittest.TestCase):
    def test_move_long_snake(self):
        """
        Currently the snake consists only of one segment. You need to update the
        `move_snake` method to also move longer snakes. It seem tricky but if you
        think carefully you will notice that it is not necessary to move all the
        segments. In fact, only the new head position and the last segment are
        important. When the snake moves the last segment needs be removed and all
        the remaining segments need to be attached to the new head. Note, that it
        also handles a case when the snake consists of only one segment.
        """
        game = SnakeGame(40, 40, snake=[(4, 3), (4, 4), (5, 4)], food=[
                         (0, 0)], direction=LEFT)
        game.move_snake()
        self.assertEqual([(3, 3), (4, 3), (4, 4)], game.snake)
        self.assertEqual([(0, 0)], game.food)

    def test_snake_eating_food(self):
        """
        When the snake encounters food it eats it and grows by one segment. A possible
        way to implement this is to update the `move_snake` method to check if the
        position of the food item is the same as the new position of the snake's head.
        If this is the case you can simply not remove the last segment of the snake and
        thus grow the snake. Also, you need to remove the food item eaten by the snake.
        """
        game = SnakeGame(40, 40, snake=[(4, 3), (4, 4), (5, 4)], food=[
                         (3, 3)], direction=LEFT)
        game.move_snake()
        self.assertEqual([(3, 3), (4, 3), (4, 4), (5, 4)], game.snake)
        self.assertNotEqual([3, 3], game.food)


if __name__ == '__main__':
    unittest.main()
