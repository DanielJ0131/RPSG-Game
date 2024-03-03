"""Test File for Unit Testing credits.py."""
# pylint: disable=import-error
import os
import sys
import unittest
from credits import Credits


def main():
    """Run the test."""
    unittest.main()


def clear_screen():
    """Clear the screen based on the operating system."""
    if sys.platform.startswith('win'):
        os.system('cls')  # for Windows
    else:
        os.system('clear')  # for Linux and macOS


class MenuTest(unittest.TestCase):
    """Test the Menu class."""

    def setUp(self):
        """Set the MenuTest."""
        self.credits = Credits()

    def test_menu(self):
        """Test the Menu class."""
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
