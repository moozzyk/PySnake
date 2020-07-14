import unittest
from SnakeGame import SnakeGame, UP, DOWN, RIGHT, LEFT


class TestSnakeGame02(unittest.TestCase):
    def test_move_snake_added(self):
        """
        Add a new method called `move_snake` that takes `self` as the only parameter
        and set the method body to `pass` like this:

        def move_snake(self):
            pass

        This method will be used to move the snake around
        """
        game = SnakeGame(10, 15)
        game.move_snake()

    def test_move_snake_head(self):
        """
        Replace the body of the move_snake method (i.e. `pass`) with the logic that moves the snake.
        For now we only care about small snake that consits only of the head. Use the direction
        class variable (i.e. `self.direction`) to decide which way to move the snake. You can use `UP`,
        `DOWN`, `RIGHT` and `LEFT` to check the direction.
        Note that the pair containing the coordinates is not mutable - you need to create a new pair
        and replace existing one with the new one
        """
        game = SnakeGame(10, 15, direction=UP, food=[(0, 0)])
        game.move_snake()
        self.assertEqual([(5, 6)], game.snake)

        game = SnakeGame(10, 15, direction=DOWN, food=[(0, 0)])
        game.move_snake()
        self.assertEqual([(5, 8)], game.snake)

        game = SnakeGame(10, 15, direction=LEFT, food=[(0, 0)])
        game.move_snake()
        self.assertEqual([(4, 7)], game.snake)

        game = SnakeGame(10, 15, direction=RIGHT, food=[(0, 0)])
        game.move_snake()
        self.assertEqual([(6, 7)], game.snake)


if __name__ == '__main__':
    unittest.main()
