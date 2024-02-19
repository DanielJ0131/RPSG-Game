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

    # self.assertEqual(player.choice, None)
    # self.assertIn(computer.choice, ["Rock", "Paper", "Scissors", "Gun"])
