"""Test File for Unit Testing player.py."""
# pylint: disable=import-error
import unittest
from player import Player


def main():
    """Run the test."""
    unittest.main()


class PlayerTest(unittest.TestCase):
    """Test the Player class."""

    def setUp(self):
        """Set the PlayerTest."""
        self.player = Player()

    def test_player(self):
        """Test the Player class."""
        self.assertIsInstance(self.player, Player)

    # def test_get_choice(self):
    #     """Test get_choice method."""
    #     self.player.set_choice()
    #     self.assertTrue(isinstance(self.player.get_choice(), str))

    # def test_set_choice(self):
    #     """Test the set_choice method."""
    #     self.player.set_choice("rock")
    #     self.assertEqual(self.player.get_choice(), "rock")
    #     self.player.set_choice("paper")
    #     self.assertEqual(self.player.get_choice(), "paper")
    #     self.player.set_choice("scissors")
    #     self.assertEqual(self.player.get_choice(), "scissors")
    #     self.player.set_choice("gun")
    #     self.assertEqual(self.player.get_choice(), "gun")

    # def test_set_name(self):
    #     """Test the set_name method."""
    #     self.player.set_name("Daniel")
    #     self.assertEqual(self.player.get_name(), str)
    #     self.player.set_name("Mi")
    #     self.assertEqual(self.player.get_name(), str)
    #     self.player.set_name("Chris")
    #     self.assertEqual(self.player.get_name(), str)

    # def test_get_name(self):
    #     """Test get_name method."""
    #     self.player.set_name("Daniel")
    #     self.assertTrue(isinstance(self.player.get_name(), str))
    #     self.player.set_name("Mi")
    #     self.assertTrue(isinstance(self.player.get_name(), str))
    #     self.player.set_name("Chris")
    #     self.assertTrue(isinstance(self.player.get_name(), str))


if __name__ == "__main__":
    main()
