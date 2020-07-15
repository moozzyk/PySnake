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

    def test_tick_added(self):
        """
        Add a new method called `tick` that only takes `self` as parameter. Invoke the `move_snake` method
        from this method.
        """
        game = SnakeGame(10, 15, direction=UP, food=[(0, 0)])
        game.tick()
        self.assertEqual([(5, 6)], game.snake)

    def test_change_direction_added(self):
        """
        Add a new method called `change_direction` that takes `self` and `new_direction` as the parameters.
        Think how the snake should change the direction. If it is going up it should only change the direction if
        the new direction is left or right (changing from up to up is no change and if you change from up to down
        it would immediately eat itself). Similarly, when the snake is going left (or right) the only effective
        change should be up or down. Calculate the new direction and set it to the `direction` class variable.
        Note that UP, RIGHT, DOWN, LEFT are actually integer variables (i.e. numbers). Can you exploit this fact
        to create a concise implementation?
        """
        # Verify direction not changed when new direction is same or the opposite
        game = SnakeGame(10, 15, direction=UP)
        game.change_direction(UP)
        self.assertEqual(UP, game.direction)
        game.change_direction(DOWN)
        self.assertEqual(UP, game.direction)

        game = SnakeGame(10, 15, direction=DOWN)
        game.change_direction(UP)
        self.assertEqual(DOWN, game.direction)
        game.change_direction(DOWN)
        self.assertEqual(DOWN, game.direction)

        game = SnakeGame(10, 15, direction=LEFT)
        game.change_direction(LEFT)
        self.assertEqual(LEFT, game.direction)
        game.change_direction(RIGHT)
        self.assertEqual(LEFT, game.direction)

        game = SnakeGame(10, 15, direction=RIGHT)
        game.change_direction(LEFT)
        self.assertEqual(RIGHT, game.direction)
        game.change_direction(RIGHT)
        self.assertEqual(RIGHT, game.direction)

        # Verify turns - counterclockwise
        game = SnakeGame(10, 15, direction=UP)
        game.change_direction(LEFT)
        self.assertEqual(LEFT, game.direction)
        game.change_direction(DOWN)
        self.assertEqual(DOWN, game.direction)
        game.change_direction(RIGHT)
        self.assertEqual(RIGHT, game.direction)
        game.change_direction(UP)
        self.assertEqual(UP, game.direction)

        # Verify turns clockwise
        game.change_direction(RIGHT)
        self.assertEqual(RIGHT, game.direction)
        game.change_direction(DOWN)
        self.assertEqual(DOWN, game.direction)
        game.change_direction(LEFT)
        self.assertEqual(LEFT, game.direction)
        game.change_direction(UP)
        self.assertEqual(UP, game.direction)


if __name__ == '__main__':
    unittest.main()
