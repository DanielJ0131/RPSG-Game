"""Scoreboard Module."""
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

import pickle  # Import the pickle module to save the game stats.


class Scoreboard:
    """Scoreboard Class."""

    def draw(self):
        """Draws the game scoreboard."""
        score_dict = self.get_score()

        print(Fore.LIGHTYELLOW_EX + "===================================")
        print(Fore.LIGHTYELLOW_EX + "|           *" + Fore.MAGENTA+ "Scoreboard" + Fore.LIGHTYELLOW_EX + "*           |")
        print(Fore.LIGHTYELLOW_EX + "===================================")
        print(Fore.LIGHTYELLOW_EX + "| " + Fore.MAGENTA + "Player names" + Fore.MAGENTA + "           Win count" + Fore.LIGHTYELLOW_EX + " |")
        print(Fore.LIGHTYELLOW_EX + "===================================")
        # Sort the stats by win count.
        if score_dict is None:
            print(Fore.LIGHTYELLOW_EX + "| -                      -         |")
        else:
            score_dict = sorted(score_dict.items(),
                                key=lambda x: x[1], reverse=True)
            for key, value in score_dict:
                print(Fore.LIGHTYELLOW_EX + f"| {key:22} {value:<9} |")
        print(Fore.LIGHTYELLOW_EX + "===================================")
        print("\n")

    def save_score(self, player, score):
        """Save the scores in a binary file."""
        if player is None:
            score_dict = None
        else:
            score_dict = {player: score}
            old_score = self.get_score()
            if old_score is not None:
                old_score.update(score_dict)
                with open("src/rpsg/scoreboard.dat", "wb") as outfile:
                    pickle.dump(old_score, outfile)
            else:
                with open("src/rpsg/scoreboard.dat", "wb") as outfile:
                    pickle.dump(score_dict, outfile)

    def get_score(self):
        """Get the scores from the binary file."""
        try:
            with open("src/rpsg/scoreboard.dat", "rb") as infile:
                score_dict = pickle.load(infile)
                return score_dict
        except (EOFError, FileNotFoundError):
            print("No scores found!")
            return None

    def __str__(self):
        """Return the string representation of the class."""
        return "Scoreboard"
