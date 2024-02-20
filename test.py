"""Test File for Unit Testing Code"""
import main
# python -m unittest --help
# python -m unittest discover
# python -m unittest discover -v
# No Assertions, no test case, no test suite, no test runner.


def test_init_default_objects():
    """Test the default objects"""
    player = main.Player()
    computer = main.Computer()
    game = main.Game()
    assert player.choice is None
    assert computer.choice in ["Rock", "Paper", "Scissors", "Gun"]
    assert game.switch == {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper",
    }


def test_roll_a_dice(self):
    """Test the roll_a_dice function"""
    assert main.Game().roll_dice in range(1, 7)
    self.assertEqual(main.Game().roll_dice, 1)
    self.assertEqual(main.Game().roll_dice, 2)
    self.assertEqual(main.Game().roll_dice, 3)
    self.assertEqual(main.Game().roll_dice, 4)
    self.assertEqual(main.Game().roll_dice, 5)
    self.assertEqual(main.Game().roll_dice, 6)


def test_game_functions(self):
    """Tests the game functions"""
    player = main.Player()
    computer = main.Computer()
    game = main.Game()
    self.assertEqual(player.choice, None)
    self.assertIn(computer.choice, ["Rock", "Paper", "Scissors", "Gun"])
    self.assertIsInstance(game.switch, dict)
    self.assertEqual(game.switch, {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper",
    })
