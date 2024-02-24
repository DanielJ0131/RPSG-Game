"""Scoreboard Module."""


class Scoreboard:
    """Scoreboard Class."""

    score = 0

    def draw(self, players):
        """Draws the game scoreboard."""
        print("Scoreboard")
        print(f"Score: {self.score}")
        for player in players:
            print(player)  # <-------------------- here is a list of players

    def __str__(self):
        return "Scoreboard"
