"""Test File for Unit Testing computer.py."""
import unittest
from computer import Computer


def main():
    """Run the test."""
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
        self.computer.set_choice()
        self.assertTrue(isinstance(self.computer.get_choice(), str))

    def test_set_choice(self):
        """Test the set_choice method."""
        for _ in range(100):
            self.computer.set_choice()
            self.assertIn(self.computer.get_choice(), ["rock", "paper",
                                                       "scissors", "gun"])

    def test_easy_choice(self):
        """Test the easy_choice method."""
        self.computer.easy_choice()
        self.assertEqual(self.computer.easy_choice(), "rock")

    def test_hard_choice(self):
        """Test the hard_choice method."""
        for _ in range(100):
            self.computer.hard_choice()
            self.assertIn(self.computer.hard_choice(), ["rock", "paper",
                                                        "scissors", "win"])


if __name__ == "__main__":
    main()
