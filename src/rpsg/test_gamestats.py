"""Test File for Unit Testing gamestats.py."""

# pylint: disable=import-error
import unittest
from gamestats import GameStats


def main():
    """Run the test."""
    unittest.main()


class GameStatsTest(unittest.TestCase):
    """Test the GameStats class."""

    def setUp(self):
        """Set the GameStats class."""
        self.game_stats = GameStats()

    def test_game_stats(self):
        """Test the GameStats class."""
        self.assertIsInstance(self.game_stats, GameStats)

    def test_win(self):
        """Test the win method."""
        self.assertEqual(self.game_stats.win(), None)
        self.assertEqual(self.game_stats.wincount, 1)

    def test_lose(self):
        """Test the lose method."""
        self.assertEqual(self.game_stats.lose(), None)
        self.assertEqual(self.game_stats.losecount, 1)

    def test_tie(self):
        """Test the tie method."""
        self.assertEqual(self.game_stats.tie(), None)
        self.assertEqual(self.game_stats.tiecount, 1)

    def test_cheater(self):
        """Test the cheater method."""
        self.assertEqual(self.game_stats.cheater(), None)
        self.assertEqual(self.game_stats.cheat, True)

    def test_add_count(self):
        """Test the add_count method."""
        self.assertEqual(self.game_stats.add_count(), None)
        self.assertEqual(self.game_stats.gamecount, 1)

    def test_print_stats(self):
        """Test the print_stats method."""
        # This method has a time.sleep() function and is not testable.

    def test_reset_stats(self):
        """Test the reset_stats method."""
        self.assertEqual(self.game_stats.reset_stats(), None)
        self.assertEqual(self.game_stats.wincount, 0)
        self.assertEqual(self.game_stats.losecount, 0)
        self.assertEqual(self.game_stats.tiecount, 0)
        self.assertEqual(self.game_stats.gamecount, 0)
        self.assertEqual(self.game_stats.cheat, False)

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.game_stats), "GameStats")


if __name__ == "__main__":
    main()
