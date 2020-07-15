import unittest
from SnakeGame import SnakeGame

"""
After you make these tests pass and run the game you will see a food item show up in the arena.
"""


class TestSnakeGame03(unittest.TestCase):
    def test_add_food_if_needed_added(self):
        """
        Add a new method called `add_food_if_needed` that takes self as the only parameter.
        It will add food that the snake can eat. Food items are stored in the list as coordinates
        - similarly to snake segments. We will allow only one food item at the time to be
        avaiable for the snake. You need to add logic that prevents adding food if not all
        the food is eaten. The easiest way to do this is to return from the function if no
        food needs to be added.
        """
        game = SnakeGame(10, 15, food=[(2, 5)])
        game.add_food_if_needed()
        self.assertEqual([(2, 5)], game.food)

    def test_new_food_added(self):
        """
        Now you need to add logic to the `add_food_if_needed` method to add food if the snake
        ate all food. You need to think carefuly where to add the food. We want to add the
        the food item in a random location. However it has to be within the board. In addition,
        you want to avoid a situation when the food would be placed on a snake.
        References:
         - randint: https://docs.python.org/3/library/random.html
        """

        for _ in range(10):
            game = SnakeGame(2, 1, snake=[(0, 0)])
            game.food = []
            game.add_food_if_needed()
            self.assertEqual([(1, 0)], game.food)

    def test_food_added_in_init(self):
        """
        There should be food for the snake ready when the game starts. You need to update the
        __init__ method to place food for the snake. The easiest way sould be to call the newly
        added `add_food_if_needed` method. However, you need to be careful where you add this
        invocation (can you put food before the snake?)
        """
        for _ in range(10):
            game = SnakeGame(2, 1, snake=[(0, 0)])
            self.assertEqual([(1, 0)], game.food)

    @unittest.skip('Remove this line AFTER implementing the fix or your code might loop forever')
    def test_food_not_added_if_no_space(self):
        """
        There is one more possibility that needs to be handled. If the player beats the game the snake
        will take all the available space. When this happens it will be impossible to add more food.
        If the `add_food_if_needed` method is trying to add food in a loop this loop will never end and
        the game will hang. You need to make sure that no attempt to add food is made if there is no
        space for the food.
        NOTE: If running tests hangs it is likely that the functionality is not implemented correctly
        and your code entered an inifinite loop (i.e. your loop inside `add_food_if_needed` never finishes).
        If this happens press CRTL+C to break the tests then fix the code and retry.
        """
        game = SnakeGame(2, 2, snake=[(0, 0), (0, 1), (1, 1), (1, 0)])
        self.assertEqual([], game.food)
        game.add_food_if_needed()
        self.assertEqual([], game.food)


if __name__ == '__main__':
    unittest.main()
