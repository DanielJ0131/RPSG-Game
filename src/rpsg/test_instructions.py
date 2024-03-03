"""Test File for Unit Testing instructions.py."""
# pylint: disable=import-error
import os
import sys
import unittest
from instructions import Instructions


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
        self.instructions = Instructions()

    def test_menu(self):
        """Test the Menu class."""
        self.assertIsInstance(self.instructions, Instructions)

    def test_draw(self):
        """Test the draw method."""
        self.assertEqual(self.instructions.draw(), None)
        clear_screen()

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.instructions), "Instructions")


if __name__ == "__main__":
    main()
