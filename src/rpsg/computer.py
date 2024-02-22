"""Computer Module."""
import random


class Computer:
    """Computer Class."""

    def __init__(self):
        """Init for the Computer Class."""
        self.choice = None
        self.choice = random.choices(
            ["Rock", "Paper", "Scissors", "Gun"], weights=[0.3, 0.3, 0.3, 0.1]
        )[0]
