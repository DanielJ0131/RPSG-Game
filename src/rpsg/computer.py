"""Computer Module."""

import random


class Computer:
    """Computer Class."""

    def __init__(self):
        """Init for the Computer Class."""
        self.choice = None
        self.mode = None

    def get_choice(self):
        """Get the computer's choice."""
        return self.choice

    def easy_choice(self):
        """Choose easy choice."""
        self.choice = "rock"

    def medium_choice(self):
        """Choose medium choice."""
        self.choice = random.choices(
            ["rock", "paper", "scissors", "gun"],
            weights=[0.3, 0.3, 0.3, 0.1],
        )[0]

    def hard_choice(self):
        """Choose hard choice."""
        self.choice = random.choices(
            ["rock", "paper", "scissors", "win"],
            weights=[0.15, 0.15, 0.15, 0.55],
        )[0]

    def set_mode(self, mode):
        """Set the mode."""
        match mode:
            case "easy" | "e":
                self.mode = "easy"
            case "medium" | "m":
                self.mode = "medium"
            case "hard" | "h":
                self.mode = "hard"
            case _:
                self.mode = None
                print("Invalid mode, try again!")
