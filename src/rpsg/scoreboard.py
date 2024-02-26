"""Scoreboard Module."""
from gamestats import GameStats

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
        print("|Win count           Player names  |")
        print("===================================")
        for player in players:
            print(player)
            
        print(f"|                  |")
        print(f"|                  |")
        print(f"|                  |")
        print("===================================")
        print("Thank you for playing!")
         # <-------------------- here is a list of players



    def __str__(self):
        return "Scoreboard"
