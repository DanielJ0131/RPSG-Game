"""Test File for Unit Testing menu.py."""
# pylint: disable=import-error
import os
import sys
import unittest
from menu import Menu


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
        self.menu = Menu()

    def test_menu(self):
        """Test the Menu class."""
        self.assertIsInstance(self.menu, Menu)

    def test_draw(self):
        """Test the draw method."""
        self.assertEqual(self.menu.draw(), None)
        clear_screen()

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.menu), "Menu")


if __name__ == "__main__":
    main()
