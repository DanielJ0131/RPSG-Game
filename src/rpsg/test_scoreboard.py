"""Test File for Unit Testing scoreboard.py."""
# pylint: disable=import-error
import unittest
from scoreboard import Scoreboard
from test_instructions import clear_screen


def main():
    """Run the test."""
    unittest.main()


class ScoreboardTest(unittest.TestCase):
    """Test the Scoreboard class."""

    def setUp(self):
        """Set the Scoreboard class."""
        self.scoreboard = Scoreboard()

    def test_scoreboard(self):
        """Test the Scoreboard class."""
        self.assertIsInstance(self.scoreboard, Scoreboard)

    def test_draw(self):
        """Test the draw method."""
        self.assertEqual(self.scoreboard.draw(), None)
        clear_screen()

    def test_save_score(self):
        """Test the save_score method."""
        self.assertEqual(self.scoreboard.save_score("Player", 1), None)

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.scoreboard), "Scoreboard")


if __name__ == "__main__":
    main()
