"""Scoreboard Module."""

import pickle  # Import the pickle module to save the game stats.
import time  # Import the time module to add a delay to the game.


class Scoreboard:
    """Scoreboard Class."""

    score = 0

    def draw(self):
        """Draws the game scoreboard."""
        score_dict = self.get_score()

        print("===================================")
        print("|           *Scoreboard*           |")
        print("===================================")
        print("| Player names           Win count |")
        print("===================================")
        # Sort the stats by win count.
        if score_dict is None:
            print("| -                      -         |")
        else:
            score_dict = sorted(score_dict.items(),
                                key=lambda x: x[1], reverse=True)
            for key, value in score_dict:
                print(f"| {key:22} {value:<9} |")
        print("===================================")
        print("\n")
        time.sleep(5)

    def save_score(self, player, score):
        """Save the scores in a binary file."""
        if player is None:
            score_dict = None
        else:
            score_dict = {player: score}
            pickle.dump(score_dict, open("src/rpsg/scoreboard.dat", "ab"))

    def get_score(self):
        """Get the scores from the binary file."""
        try:
            with open("src/rpsg/scoreboard.dat", "rb") as infile:
                while True:
                    try:
                        score_dict = pickle.load(infile)
                        return score_dict
                    except EOFError:
                        break
        except FileNotFoundError:
            print("No scores found!")
