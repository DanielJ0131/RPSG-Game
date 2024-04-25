"""Scoreboard Module."""

import pickle  # Import the pickle module to save the game stats.


class Scoreboard:
    """Scoreboard Class."""

    def __init__(self):
        """Initialize the class."""
        self.score_dict = None

    def draw(self):
        """Draws the game scoreboard."""
        score_dict = self.get_score()
        self.score_dict = score_dict

        print(" ==================================")
        print("|           *Scoreboard*           |")
        print(" ==================================")
        print("| Player                 Win count |")
        print(" ==================================")
        if score_dict is None:
            print("| -                      -         |")
        else:
            # Sort the stats by win count.
            score_dict = sorted(score_dict.items(), key=lambda x: x[1],
                                reverse=True)
            for key, value in score_dict:
                print(f"| {key:22} {value:<9} |")
        print(" ==================================")
        print("\n")
        self.score_dict = score_dict

    def save_score(self, player, score):
        """Save the scores in a binary file."""
        if player is None:
            score_dict = None
        else:
            score_dict = {player: score}
            old_score = self.get_score()
            if old_score is not None:
                old_score.update(score_dict)
                with open("scoreboard.bin", "wb") as outfile:
                    pickle.dump(old_score, outfile)
            else:
                with open("scoreboard.bin", "wb") as outfile:
                    pickle.dump(score_dict, outfile)
        self.score_dict = score_dict

    def get_score(self):
        """Get the scores from the binary file."""
        score_dict = self.score_dict
        try:
            with open("scoreboard.bin", "rb") as infile:
                score_dict = pickle.load(infile)
                return score_dict
        except (EOFError, FileNotFoundError):
            print("No scores found!")
            return None

    def __str__(self):
        """Return the string representation of the class."""
        return "Scoreboard"
