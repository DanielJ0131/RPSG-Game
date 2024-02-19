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


def test_roll_a_dice():
    """Test the roll_a_dice function"""
    # assert main.dice_roll in range(1, 7)
    # self.assertEqual(player.choice, None)
    # self.assertIn(computer.choice, ["Rock", "Paper", "Scissors", "Gun"])
    # self.assertIsInstance(game.switch, dict)
    # "White Box Testing"
    # self.assertEqual(main.dice_roll, 1)
    # expected = 1
    # result = 1
    # self.assertEqual(res
    # actual = main.dice_roll
    # test_addition(expected, actual)
    # good to call these functions "test" because it's a test file


def unittest_skip():
    """Test the skip function"""
    # self.skipTest("Skip this test")
