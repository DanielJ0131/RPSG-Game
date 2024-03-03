"""Test File for Unit Testing menu.py."""
import unittest
from menu import Menu


def main():
    """Run the test."""
    unittest.main()


class MenuTest(unittest.TestCase):
    """Test the Menu class."""

    def test_set_up(self):
        """Set the MenuTest."""
        self.menu = Menu()

    def test_menu(self):
        """Test the Menu class."""
        self.assertIsInstance(self.menu, Menu)


if __name__ == "__main__":
    main()
