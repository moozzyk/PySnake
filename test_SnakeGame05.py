import unittest
from SnakeGame import SnakeGame, PLAYING, GAME_OVER, GAME_WON, UP, RIGHT, DOWN, LEFT

"""
After you make these tests pass and run the game the snake will no
longer be immortal and will not be able to leave the screen.
"""


class TestSnakeGame05(unittest.TestCase):
    def test_status_added(self):
        """
        Create a new class variable called `status` and initialize it to
        the value `PLAYING` defined on line 8. This variable will be used
        to get current status of the game.
        """
        game = SnakeGame(10, 15)
        self.assertEqual(PLAYING, game.status)

    def test_game_over_if_snake_runs_into_border(self):
        """
        Update the `tick` method to check if the snake hit the border when
        moving. If so, update the status to `GAME_OVER`.
        """
        game = SnakeGame(5, 5, snake=[(5, 0)], direction=UP)
        game.tick()
        self.assertEqual(GAME_OVER, game.status)

        game = SnakeGame(10, 15, snake=[(0, 5)], direction=LEFT)
        game.tick()
        self.assertEqual(GAME_OVER, game.status)

        game = SnakeGame(10, 15, snake=[(9, 5)], direction=RIGHT)
        game.tick()
        self.assertEqual(GAME_OVER, game.status)

        game = SnakeGame(10, 15, snake=[(14, 5)], direction=DOWN)
        game.tick()
        self.assertEqual(GAME_OVER, game.status)

        game = SnakeGame(10, 15, snake=[(1, 5)], direction=DOWN)
        game.tick()
        self.assertEqual(PLAYING, game.status)

    def test_tick_is_no_op_when_status_GAME_OVER(self):
        game = SnakeGame(10, 15, snake=[(0, 0)], direction=UP)
        game.tick()
        self.assertEqual(GAME_OVER, game.status)
        saved_snake = game.snake
        game.tick()
        self.assertEqual(GAME_OVER, game.status)
        self.assertEqual(saved_snake, game.snake)


if __name__ == '__main__':
    unittest.main()
