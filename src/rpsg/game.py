"""Game Module."""

import time  # Import the time module to add a delay to the game.
import random
from player import Player
from computer import Computer
from gamestats import GameStats
from scoreboard import Scoreboard


class Game:
    """Game Class."""

    def __init__(self):
        """Init for the Game Class."""
        self.switch = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }

    def play(self, rounds):
        """Play the game."""
        print("\nWelcome to Rock, Paper, Scissors, Gun!")
        best_of_rounds = (rounds // 2) + 1

        game = GameStats(best_of_rounds)

        while (game.wincount or game.losecount) < best_of_rounds:
            game.add_count()

            # Player and Computer choices #
            player = Player().set_choice()
            computer = Computer().set_choice()

            # Game Logic #
            # If the player and computer chose the same thing, it's a tie.

            if player == "gun":
                print("I give up, you win, I do not want to play!!!")
                game.win()
                
                self.announce_winner(game, best_of_rounds)
                print("(You have been banished " +
                      "from this game and have to reset)")
                time.sleep(5)
                break

            print(f"Computer chose: {computer}!")
            time.sleep(1)

            if player == computer:
                print("It's a tie!")
                game.tie()
                time.sleep(1)

            # If the computer chose Gun, the player has to roll the dice.
            elif computer == "gun":
                print(
                    "The computer chose Gun! " +
                    "Roll the dice to see if you survive! "
                )
                self.roll_dice(game, player)
                time.sleep(1)

            # If the player chose the losing choice, they lose.
            elif player == self.switch[computer]:
                print("You lose!")
                game.lose()
                time.sleep(1)

            # If the player chose the winning choice, they win.
            else:
                print("You win!")
                game.win()
                time.sleep(1)

            if game.wincount >= best_of_rounds or \
               game.losecount >= best_of_rounds:
                self.announce_winner(game, best_of_rounds)
                time.sleep(1)

    def roll_dice(self, game, player):
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

        if dice >= 4:
            game.win()
            if player == "scissors":
                print("You cut the Gun in half and won!")

            elif player == "rock":
                print("You smashed the Gun and won!")

            elif player == "paper":
                print("You pushed the Paper into " + "the Gun and won!")

        else:
            print("You lost! Better luck next time.")
            game.lose()

    def announce_winner(self, game, best_of_rounds):
        list_score = []
        """Check who is the winner."""
        print("\nWe have a winner!")
        time.sleep(1)
        if game.wincount >= best_of_rounds:
            print("\nand it's the user!")

        elif game.losecount >= best_of_rounds:
            print("\nand it's the computer!")

        elif game.winfast >= best_of_rounds:
            print("\nand it's the user")

        rematch = input("\nWanna play again? , yes/no: ")

        if rematch.lower() in ["no", "n"]:
            if game.winfast >= best_of_rounds:
                print("(WARNING: You cheated in this game >:C)")
            else:
                print("Good game :)")

            # Game stats #
            time.sleep(2)
            game.print_stats()
            list_score.append(game.print_stats)

        else:
            print("Rematch!")
            time.sleep(2)
            game.reset_stats()
