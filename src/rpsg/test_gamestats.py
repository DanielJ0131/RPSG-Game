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
        self.GameStats = GameStats()

    def test_GameStats(self):
        """Test the GameStats class."""
        self.assertIsInstance(self.GameStats, GameStats)

    def test_win(self):
        """Test the win method."""
        self.assertEqual(self.GameStats.win(), None)

    def test_lose(self):
        """Test the lose method."""
        self.assertEqual(self.GameStats.lose(), None)

    def test_tie(self):
        """Test the tie method."""
        self.assertEqual(self.GameStats.tie(), None)

    def test_cheater(self):
        """Test the cheater method."""
        self.assertEqual(self.GameStats.cheater(), None)
    
    def test_add_count(self):
        """Test the add_count method."""
        self.assertEqual(self.GameStats.add_count(), None)
    
    def test_print_stats(self):
        """Test the print_stats method."""
        self.assertEqual(self.GameStats.print_stats(), None)
    
    def test_reset_stats(self):
        """Test the reset_stats method."""
        self.assertEqual(self.GameStats.reset_stats(), None)

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.GameStats), "GameStats")


if __name__ == "__main__":
    main()
