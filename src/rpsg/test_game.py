"""Test File for Unit Testing game.py."""
# pylint: disable=import-error
from unittest import mock
import unittest
from test_instructions import clear_screen
from game import Game


def main():
    """Run the test."""
    unittest.main()


class GameTest(unittest.TestCase):
    """Test the Game class."""

    def setUp(self):
        """Set up the Game class."""
        self.game = Game()

    def test_game(self):
        """Test the game class."""
        self.assertIsInstance(self.game, Game)

    def test_init(self):
        """Test the __init__ method."""
        self.assertEqual(self.game.switch, {'rock': 'scissors',
                                            'paper': 'rock',
                                            'scissors': 'paper'})

    def test_roll_dice(self):
        """Test the roll_dice method."""
        # Mock user input
        with mock.patch('builtins.input', return_value='rock'):
            self.assertIn(self.game.roll_dice(), [1, 2, 3, 4, 5, 6])
        clear_screen()


if __name__ == "__main__":
    main()
