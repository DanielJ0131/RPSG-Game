"""Player Class."""


class Player:
    """Player Class."""

    def __init__(self):
        """Init for the Player Class."""
        self.choice = None

    def get_choice(self):
        """Get the player's choice."""
        return self.choice

    def set_choice(self):
        """Set the player's choice."""
        while self.choice not in ["Rock", "Paper", "Scissors", "Gun"]:
            print('\nChoose "Rock", "Paper", "Scissors" to play!')
            self.choice = input("\nEnter your choice >>> ").lower()
            match self.choice:
                case "rock"|"r":
                    self.choice = "rock"
                case "paper"|"p":
                    self.choice = "paper"
                case "scissors"|"s":
                    self.choice = "scissors"
                case "gun"|"g":
                    self.choice = "gun"
            return self.choice

      