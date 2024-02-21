"""Player Class."""


class Player:
    """Player Class."""

    def __init__(self):
        """Init for the Player Class."""
        self.choice = None
        while self.choice not in ["Rock", "Paper", "Scissors"]:
            print('\nChoose "Rock", "Paper", or "Scissors" to play!')
            self.choice = input("\nEnter your choice >>> ")
