"""Test File for Unit Testing game.py."""
# pylint: disable=import-error
import unittest
from game import Game


def main():
    """Run the test."""
    unittest.main()


class GameTest(unittest.TestCase):
    """Test the Game class."""

    def setUp(self):
        """Set the Game class."""
        self.game = Game()

    def test_game(self):
        """Test the game class."""
        self.assertIsInstance(self.game, Game)

    def test_init(self):
        """Test the __init__ method."""
        self.assertEqual(self.game.switch, {'rock': 'scissors',
                                            'paper': 'rock',
                                            'scissors': 'paper'})


if __name__ == "__main__":
    main()
