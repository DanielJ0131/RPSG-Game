"""Test File for Unit Testing instructions.py."""
# pylint: disable=import-error
import unittest
from instructions import Instructions


def main():
    """Run the test."""
    unittest.main()


class InstructionsTest(unittest.TestCase):
    """Test the Instructions class."""

    def setUp(self):
        """Set the Instructions class."""
        self.instructions = Instructions()

    def test_instructions(self):
        """Test the Instructions class."""
        self.assertIsInstance(self.instructions, Instructions)

    def test_draw(self):
        """Test the draw method."""
        self.assertEqual(self.instructions.draw(), None)
        Instructions().clear_screen()

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.instructions), "Instructions")


if __name__ == "__main__":
    main()
