"""Instructions Module."""


class Instructions:
    """Instructions Class."""

    def __init__(self):
        """Init for the Instruction Class."""

    def draw(self):
        """Draws the game Instruction."""
        print(
            """
              How to Play the game step by step:
              * Game is simple and similar to Rock, Paper, Scissors.
              * If you have played this game before, skip these instructions.
              * To Start, select 1 on the main menu and press enter.
              * The player will go up against a computer bot.
              * The player can choose difficulty level. (Easy, Medium, Hard)
              * The player then has the options Rock, Paper, Scissors or Gun.
              * You can also type (r, p, s, g) to choose your option.
              * Gun for player is a cheat code to automatically win.
              * The computer has a 10% chance of choosing Gun.
              * If the computer chooses Gun, the player rolls a dice to win.
              * Whoever takes the winning choice, wins the round.
              * This continues until anyone wins more than 4 rounds.
              * The score will show you the results at the end of the rounds.
              * You can either beat the computer, lose or play again.
              * Good luck and have fun!

              """
        )

    def __str__(self):
        """Return the class name."""
        return "Instructions"
