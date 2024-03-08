"""Test File for Unit Testing scoreboard.py."""

# pylint: disable=import-error
import os  # Import the os module to remove the scoreboard.bin file.
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
        self.assertEqual(self.scoreboard.save_score(None, 1), None)
        if os.path.exists("scoreboard.bin"):
            os.remove("scoreboard.bin")
        self.assertEqual(self.scoreboard.save_score("Daniel", 3), None)
        clear_screen()

    def test_get_score(self):
        """Test the get_score method."""
        if os.path.exists("scoreboard.bin"):
            os.remove("scoreboard.bin")
        self.scoreboard.score_dict = None
        self.assertEqual(self.scoreboard.get_score(), None)
        self.assertEqual(self.scoreboard.score_dict, None)
        self.test_save_score()
        self.assertIsInstance(self.scoreboard.get_score(), dict)
        self.assertEqual(self.scoreboard.get_score(), {"Daniel": 3})
        self.assertEqual(self.scoreboard.score_dict, {"Daniel": 3})
        clear_screen()

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.scoreboard), "Scoreboard")


if __name__ == "__main__":
    main()
