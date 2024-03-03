"""Test File for Unit Testing computer.py."""
# pylint: disable=import-error
import unittest
from computer import Computer


def main():
    """Run the test."""
    ComputerTest().setUp()
    unittest.main()


class ComputerTest(unittest.TestCase):
    """Test the Computer class."""

    def setUp(self):
        """Set the ComputerTest."""
        self.computer = Computer()

    def test_computer(self):
        """Test the Computer class."""
        self.assertIsInstance(self.computer, Computer)

    def test_get_choice(self):
        """Test get_choice method."""
        self.computer.medium_choice()
        self.assertTrue(isinstance(self.computer.get_choice(), str))

    def test_medium_choice(self):
        """Test the medium_choice method."""
        self.computer.medium_choice()
        self.assertIn(self.computer.get_choice(), ["rock", "paper",
                                                   "scissors", "gun"])

    def test_easy_choice(self):
        """Test the easy_choice method."""
        self.computer.easy_choice()
        self.assertEqual(self.computer.get_choice(), "rock")

    def test_hard_choice(self):
        """Test the hard_choice method."""
        self.computer.hard_choice()
        self.assertIn(self.computer.get_choice(), ["rock", "paper",
                                                   "scissors", "win"])

    def test_set_mode(self):
        """Test the set_mode method."""
        # Easy #
        self.computer.set_mode("easy")
        self.assertEqual(self.computer.mode, "easy")
        self.computer.set_mode("e")
        self.assertEqual(self.computer.mode, "easy")
        # Medium #
        self.computer.set_mode("medium")
        self.assertEqual(self.computer.mode, "medium")
        self.computer.set_mode("m")
        self.assertEqual(self.computer.mode, "medium")
        # Hard #
        self.computer.set_mode("hard")
        self.assertEqual(self.computer.mode, "hard")
        self.computer.set_mode("h")
        self.assertEqual(self.computer.mode, "hard")
        # Invalid #
        self.computer.set_mode("invalid")
        self.assertEqual(self.computer.mode, None)


if __name__ == "__main__":
    main()
