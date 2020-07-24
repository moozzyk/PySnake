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

    def test_game_over_if_snake_runs_into_itself(self):
        """
        Update the `tick` method to check if the snake hit its tail when moving
        If so, update the status to `GAME_OVER`.
        """
        game = SnakeGame(10, 15, snake=[
                         (5, 6), (5, 5), (6, 5), (7, 5), (7, 6), (7, 7), (6, 7), (5, 7), (4, 7)], direction=DOWN)
        game.tick()
        self.assertEqual(GAME_OVER, game.status)

    def test_tick_is_no_op_when_status_GAME_OVER(self):
        """
        If the game is finished nothing should happen even if the `tick()` method is called.
        The easiest way to fix it is to check the game status in the `tick()` method and
        return immediately from the method if needed.
        """
        game = SnakeGame(10, 15, snake=[(0, 0)], direction=UP)
        game.tick()
        self.assertEqual(GAME_OVER, game.status)
        saved_snake = game.snake
        game.tick()
        self.assertEqual(GAME_OVER, game.status)
        self.assertEqual(saved_snake, game.snake)

    def test_the_game_is_won_if_there_are_no_more_empty_spaces_on_the_board(self):
        """
        In the case the snake occupies all the tiles and there is no space to place any new food
        the player wins the game. If this happens the game status should be changed to GAME_WON.
        """
        game = SnakeGame(2, 1, snake=[(0, 0)], direction=RIGHT)
        game.tick()
        self.assertEqual(GAME_WON, game.status)
        self.assertEqual([], game.food)

    def test_tick_is_no_op_when_status_GAME_WON(self):
        """
        If the game is won nothing should happen even if the `tick()` method is called.
        The easiest way to fix it is to check the game status in the `tick()` method and
        return immediately from the method if needed.
        """
        game = SnakeGame(2, 1, snake=[(0, 0)], direction=RIGHT)
        game.tick()
        self.assertEqual(GAME_WON, game.status)
        saved_snake = game.snake
        game.tick()
        self.assertEqual(saved_snake, game.snake)


if __name__ == '__main__':
    unittest.main()
