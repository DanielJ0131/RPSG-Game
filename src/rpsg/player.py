"""Player Class."""


class Player:
    """Player Class."""

    def __init__(self):
        """Init for the Player Class."""
        self.choice = None
        self.name = None

    def get_name(self):
        """Get the player's name."""
        return self.name

    def set_name(self, name):
        """Set the player's name."""
        self.name = name

    def input_name(self):
        """Input the player's name."""
        while True:
            name = input("Enter player name: ")
            if len(name) >= 10:
                print("\n(Your name is too long!)")
                continue
            print(f"\nAre you happy with the name: {name}?")
            answer = input("(yes/no) >>> ").lower()
            if answer in ["yes", "y"]:
                self.set_name(name)
                break

    def get_choice(self):
        """Get the player's choice."""
        return self.choice

    def set_choice(self):
        """Set the player's choice."""
        self.choice = None
        while self.choice not in ["rock", "paper", "scissors", "gun"]:
            print('\nChoose "Rock", "Paper", "Scissors" to play!')
            self.choice = input("\nEnter your choice >>> ").lower()
            match self.choice:
                case "rock" | "r":
                    self.choice = "rock"
                case "paper" | "p":
                    self.choice = "paper"
                case "scissors" | "s":
                    self.choice = "scissors"
                case "gun" | "g":
                    self.choice = "gun"
                case _:
                    self.choice = None
                    print("Invalid choice, try again!")
                    continue
