"""Scoreboard Module."""


class Scoreboard:
    """Scoreboard Class."""

    score = 0

    def scorelist(self, name, wincount):
        """Saves the scores."""

    def draw(self, players):
        """Draws the game scoreboard."""
        print("===================================")
        print("|           *Scoreboard*           |")
        print("===================================")
        print("| Player names           Win count |")
        print("===================================")
        for player in players:
            print(f"| {player:32} |")

        print("===================================")
        print("\n")

    def __str__(self):
        return "Scoreboard"
