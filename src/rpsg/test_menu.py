"""Test File for Unit Testing menu.py."""

# pylint: disable=import-error
import unittest
from menu import Menu
from test_instructions import clear_screen


def main():
    """Run the test."""
    unittest.main()


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
