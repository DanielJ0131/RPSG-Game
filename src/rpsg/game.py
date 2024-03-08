"""Game Module."""

# pylint: disable=import-error
import time  # Import the time module to add a delay to the game.
import random
from scoreboard import Scoreboard
from computer import Computer
from gamestats import GameStats


class Game:
    """Game Class."""

    def __init__(self):
        """Init for the Game Class."""
        self.switch = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }

    def play(self, rounds, player):
        """Play the game."""
        # Initialize Computer and Rounds #
        computer = Computer()
        time.sleep(1)
        best_of_rounds = (rounds // 2) + 1
        print("\nWelcome to Rock, Paper, Scissors, Gun!")
        print(f"\nThe game has chosen best of {best_of_rounds} rounds!")

        # Choosee Mode #
        mode = None
        while mode not in ["easy", "medium", "hard", "e", "m", "h"]:
            mode = input("Enter mode: Easy, Medium, Hard >>> ").lower()
        computer.set_mode(mode)

        # Initialize GameStats #
        game = GameStats()

        while (game.wincount or game.losecount) < best_of_rounds:
            game.add_count()

            # Player and Computer choices #
            player.input_choice()
            match computer.mode:
                case "easy":
                    computer.easy_choice()
                case "medium":
                    computer.medium_choice()
                case "hard":
                    computer.hard_choice()

            print(f"Computer chose: {computer.get_choice().capitalize()}!")
            time.sleep(1)

            # Game Logic #

            # If the player and computer chose the same thing, it's a tie.
            if player.get_choice() == computer.get_choice():
                print("It's a tie!")
                game.tie()
                time.sleep(1)

            # If the player cheats and uses gun, they win.
            elif (player.get_choice()) == "gun":
                print("I give up, you win, I do not want to play!!!")
                game.cheater()
                game.win()
                self.announce_winner(game, best_of_rounds, player)
                print("(You have been banished " +
                      "from this game and have to reset)")
                time.sleep(5)
                break

            # If the computer chose win, it automatically wins.
            elif computer.get_choice() == "win":
                print("Auto win by computer!")
                game.lose()
                time.sleep(1)

            # If the computer chose Gun, the player has to roll the dice.
            elif computer.get_choice() == "gun":
                print(
                    "\nThe computer chose Gun! "
                    + "Roll the dice to see if you survive! "
                )

                if self.roll_dice() >= 4:
                    game.win()
                    match player.get_choice():
                        case "scissors":
                            print("You cut the Gun in half and won!")

                        case "rock":
                            print("You smashed the Gun and won!")

                        case "paper":
                            print("You pushed the Paper into the Gun and won!")

                else:
                    print("You lost! Better luck next time.")
                    game.lose()
                    time.sleep(1)

            # If the player chose the losing choice, they lose.
            elif player.get_choice() == self.switch[computer.get_choice()]:
                print("You lose!")
                game.lose()
                time.sleep(1)

            # If the player chose the winning choice, they win.
            else:
                print("You win!")
                game.win()
                time.sleep(1)

            # Check if the game is over.
            if game.wincount >= best_of_rounds or \
               game.losecount >= best_of_rounds:
                self.announce_winner(game, best_of_rounds, player)
                time.sleep(1)
                break

    def roll_dice(self):
        """Roll the dice to see if the player survives the Gun."""
        input("Press enter to roll the dice! >>> ")
        time.sleep(1)
        print("Rolling the dice.")
        time.sleep(0.250)
        print("Rolling the dice..")
        time.sleep(0.250)
        print("Rolling the dice...")
        time.sleep(0.250)
        print("Rolling the dice....")
        time.sleep(0.250)

        dice = random.randint(1, 6)
        print(f"You rolled a {dice}!!!")
        time.sleep(1)
        return dice

    def announce_winner(self, game, best_of_rounds, player):
        """Check who is the winner."""
        score = game.wincount

        print("\nWe have a winner!")
        time.sleep(1)

        if game.losecount >= best_of_rounds:
            print("\nand it's the computer!")

        else:
            print(f"\nand it's {player.get_name()}!")

        time.sleep(1)
        print("\nWanna play again?")
        rematch = None
        while rematch not in ["yes", "no", "y", "n"]:
            rematch = input("(yes/no) >>> ")

        if rematch.lower() in ["no", "n"]:
            time.sleep(2)
            if game.cheat is True:
                print("\n(WARNING: You cheated in this game >:C)")
            else:
                print("\nGood game :)")
            time.sleep(2)

            # Game stats #
            if game.cheat is False:  # If the player didn't cheat.
                Scoreboard().save_score(player.get_name(), score)  # Save.
                print("\nScore saved!")
                time.sleep(2)
            game.print_stats()  # Print the game stats.
            time.sleep(2)

        else:
            print("\nRematch!")
            time.sleep(2)
            game.reset_stats()
