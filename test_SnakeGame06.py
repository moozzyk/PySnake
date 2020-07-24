import unittest
from SnakeGame import SnakeGame, UP

"""
After you make these tests pass and run the game will track the score
earned for eating food.
"""


class TestSnakeGame06(unittest.TestCase):
    def test_score_added(self):
        """
        Create a new class variable called `score` and initialize it to 0.
        This variable will be used to keep the score.
        """
        game = SnakeGame(10, 15)
        self.assertEqual(0, game.score)

    def test_score_increased_after_eating_food(self):
        """
        Increase the score each time the snake eats a food item by 5.
        """
        game = SnakeGame(10, 15, snake=[(5, 7)], food=[(5, 6)], direction=UP)
        self.assertEqual(0, game.score)
        game.tick()
        self.assertEqual(5, game.score)
        game.tick()
        self.assertEqual(5, game.score)
        game.food = [(5, 4)]
        game.tick()
        self.assertEqual(10, game.score)


if __name__ == "__main__":
    unittest.main()
