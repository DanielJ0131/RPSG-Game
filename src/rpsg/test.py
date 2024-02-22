"""Test File for Unit Testing Code."""
from player import Player
from game import Game
from computer import Computer
# python -m unittest --help
# python -m unittest discover
# python -m unittest discover -v
# No Assertions, no test case, no test suite, no test runner.


def test_init_default_objects():
    """Test the default objects."""
    player = Player()
    computer = Computer()
    game = Game()
    assert player.choice is None
    assert computer.choice in ["Rock", "Paper", "Scissors", "Gun"]
    assert game.switch == {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper",
    }


def test_roll_a_dice(self):
    """Test the roll_a_dice function."""
    assert Game().roll_dice in range(1, 7)
    self.assertEqual(Game().roll_dice, 1)
    self.assertEqual(Game().roll_dice, 2)
    self.assertEqual(Game().roll_dice, 3)
    self.assertEqual(Game().roll_dice, 4)
    self.assertEqual(Game().roll_dice, 5)
    self.assertEqual(Game().roll_dice, 6)


def test_game_functions(self):
    """Test the game functions."""
    player = Player()
    computer = Computer()
    game = Game()
    self.assertEqual(player.choice, None)
    self.assertIn(computer.choice, ["Rock", "Paper", "Scissors", "Gun"])
    self.assertIsInstance(game.switch, dict)
    self.assertEqual(game.switch, {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper",
    })
