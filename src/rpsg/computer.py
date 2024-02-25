"""Computer Module."""
import random


class Computer:
    """Computer Class."""

    def __init__(self):
        """Init for the Computer Class."""
        self.choice = None

    def get_choice(self):
        """Get the computer's choice."""
        return self.choice

    def set_choice(self):
        """Set the computer's choice."""
        self.choice = random.choices(
            ["rock", "paper", "scissors", "gun"], weights=[0.3, 0.3, 0.3, 0.1]
            )[0]
        return self.choice
