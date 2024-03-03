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
              1. Game is simple and it's about Rock, Paper, Scissors and Gun.
              2. If you have played this game before, skip this tutorial.
              3. To Start, select 1 on the main menu and press enter.
              4. The player will go up against a computer bot.
              5. The player then has the options Rock, Paper, Scissors or Gun.
              6. The computer has a 10% chance of choosing Gun.
              7. Whoever takes the winning choice, wins the round.
              8. This continues until we anyone wins more than 3 rounds.
              9. The score will show you the results at the end of the rounds.
              10. You can either beat the computer, lose or play again.
              """
        )

    def __str__(self):
        """Return the class name."""
        return "Instructions"
