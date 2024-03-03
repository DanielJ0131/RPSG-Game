"""Test File for Unit Testing menu.py."""
# pylint: disable=import-error
import unittest
from menu import Menu


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
        self.menu.draw()
        self.assertEqual(self.menu.draw(), None)


if __name__ == "__main__":
    main()
