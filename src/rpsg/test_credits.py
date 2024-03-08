"""Test File for Unit Testing credits.py."""

# pylint: disable=import-error
import unittest
from credits import Credits
from test_instructions import clear_screen


def main():
    """Run the test."""
    unittest.main()


class CreditsTest(unittest.TestCase):
    """Test the Credits class."""

    def setUp(self):
        """Set the Credits class."""
        self.credits = Credits()

    def test_credits(self):
        """Test the Credits class."""
        self.assertIsInstance(self.credits, Credits)

    def test_draw(self):
        """Test the draw method."""
        self.assertEqual(self.credits.draw(), None)
        clear_screen()

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.credits), "Credits")


if __name__ == "__main__":
    main()
