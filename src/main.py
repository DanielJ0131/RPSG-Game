"""This is the main file for the Rock, Paper, Scissors, Gun Game."""

import random
import time  # Import the time module to add a delay to the game.


def main():
    """Use the main function."""
    lst = []
    while True:
        Menu().draw()
        choice = input("\nEnter your choice >>> ")
        match choice:
            case "1":
                while True:
                    player_name = input("Enter player name: ")
                    print(f"\nAre you happy with the name: {player_name}?")
                    answer = input("yes/no: ").lower()
                    if answer == "yes" or answer == "y":
                        lst.append(player_name)
                        break
                    elif answer == "no" or answer == "n":
                        continue
                rounds = 3  # <----------------Change the number of rounds here
                Game().play(rounds)

            case "2":
                Scoreboard().draw(lst)
                continue
            case "3":
                Instruction().draw()
                continue
            case "4":
                Credits().draw()
                break


class Player:
    """Player Class."""

    def __init__(self):
        """Init for the Player Class."""
        self.choice = None
        while self.choice not in ["Rock", "Paper", "Scissors"]:
            print('\nChoose "Rock", "Paper", or "Scissors" to play!')
            self.choice = input("\nEnter your choice >>> ")


class Computer:
    """Computer Class."""

    def __init__(self):
        """Init for the Computer Class."""
        self.choice = None
        self.choice = random.choices(
            ["Rock", "Paper", "Scissors", "Gun"], weights=[0.3, 0.3, 0.3, 0.1]
        )[0]


class Game:
    """Game Class."""

    def __init__(self):
        """Init for the Game Class."""
        self.switch = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper",
        }

    def play(self, rounds):
        """Play the game."""
        print("\nWelcome to Rock, Paper, Scissors, Gun!")
        best_of_rounds = (rounds // 2) + 1

        game = GameStats()

        while (game.wincount or game.losecount) < best_of_rounds:
            game.add_count()

            # Player and Computer choices #
            player = Player().choice
            computer = Computer().choice
            print(f"Computer chose: {computer}!")
            time.sleep(1)

            # Game Logic #
            # If the player and computer chose the same thing, it's a tie.
            if player == computer:
                print("It's a tie!")
                game.tie()
                time.sleep(1)

            # If the computer chose Gun, the player has to roll the dice.
            elif computer == "Gun":
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

            if (game.wincount >= best_of_rounds or
               game.losecount >= best_of_rounds):
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
            if player == "Scissors":
                print("You cut the Gun in half and won!")

            elif player == "Rock":
                print("You smashed the Gun and won!")

            elif player == "Paper":
                print("You pushed the Paper into " + "the Gun and won!")

        else:
            print("You lost! Better luck next time.")
            game.lose()

    def announce_winner(self, game, best_of_rounds):
        """Check who is the winner."""
        print("\nWe have a winner!")
        time.sleep(1)
        if game.wincount >= best_of_rounds:
            print("\nand it's the user!")

        elif game.losecount >= best_of_rounds:
            print("\nand it's the computer!")

        rematch = input("\nWanna play again? , yes/no: ")

        if rematch == "no" or rematch == "n":
            print("Good game :)")

            # Game stats #
            time.sleep(2)
            game.print_stats()

        else:
            print("Rematch!")
            time.sleep(2)
            game.reset_stats()


class GameStats:
    """GameStats Class."""

    def __init__(self):
        """Init for the GameStats Class."""
        self.wincount = 0
        self.losecount = 0
        self.tiecount = 0
        self.gamecount = 0

    def win(self):
        """Win Count function."""
        self.wincount += 1

    def lose(self):
        """Lose Count function."""
        self.losecount += 1

    def tie(self):
        """Tie Count function."""
        self.tiecount += 1

    def add_count(self):
        """Game Count function."""
        self.gamecount += 1

    def print_stats(self):
        """Print the game stats."""
        print("\nLatest score:")
        time.sleep(1)
        print(f"Game count: {self.gamecount}")
        time.sleep(0.5)
        print(f"Win count: {self.wincount}")
        time.sleep(0.5)
        print(f"Tie count: {self.tiecount}")
        time.sleep(0.5)
        print(f"Lose count: {self.losecount}")
        time.sleep(5)

    def reset_stats(self):
        """Reset the game stats."""
        self.wincount = 0
        self.losecount = 0
        self.tiecount = 0
        self.gamecount = 0


class Menu:
    """Menu Class."""

    def draw(self):
        """Draws the game menu."""
        print("===================================")
        print("|         Welcome to the           |")
        print("|  * Rock, Paper, Scissors, Gun *  |")
        print("|              Game!               |")
        print("|==================================|")
        print("| 1. Start Game                    |")
        print("| 2. Scoreboard                    |")
        print("| 3. Instructions                  |")
        print("| 4. Credits                       |")
        print("|==================================|")


class Instruction:
    """Instruction Class."""

    def draw(self):
        """Draws the game Instruction."""
        print(
            """
              How to Play the game step by step:
              1. Game is simple and it's about Rock, Paper, Scissors and Gun.
              2. If you have played this game before, skip this tutorial.
              3. To Start, select 1 on the main menu and press enter.
              4. The player will go up against a computer bot.
              5. The player then has the options Rock, Paper or Scissors.
              6. The computer has a 10% chance of choosing Gun.
              7. Whoever takes the winning choice, wins the round.
              8. This continues until we anyone wins more than 3 rounds.
              9. The score will show you the results at the end of the rounds.
              10. You can either beat the computer, lose or play again.
              """
            )


class Scoreboard:
    """Scoreboard Class."""

    score = 0

    def draw(self, players):
        """Draws the game scoreboard."""
        print("Scoreboard")
        print(f"Score: {self.score}")
        for player in players:
            print(player)  # <-------------------- here is a list of players


class Credits:
    """Credits Class."""

    def draw(self):
        """Draws the game credits and authors."""
        author1 = "Ngoc Hong (Mi)"
        author2 = "Chris Lubert"
        author3 = "Daniel Jönsson"
        print("===================================")
        print("|           *Credits*             |")
        print("===================================")
        print("|© HKR 2024 - All rights reserved.|")
        print("===================================")
        print("|          Created by:            |")
        print(f"|-{author1}                  |")
        print(f"|-{author2}                    |")
        print(f"|-{author3}                  |")
        print("===================================")
        print("Thank you for playing!")


if __name__ == "__main__":
    main()