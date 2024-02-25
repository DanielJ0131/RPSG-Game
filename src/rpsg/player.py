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
            if self.choice in ["r","p","s","g","rock","paper","scissors","gun"]:
                
                if self.choice == "r":
                    self.choice = "rock"
                    return self.choice
                
                elif self.choice == "p":
                    self.choice = "paper"
                    return self.choice
                
                elif self.choice == "s":
                    self.choice = "scissors"
                    return self.choice
                
                elif self.choice == "g":
                    self.choice = "gun"
                    return self.choice
                
                else:
                    return self.choice
