"""This is the main file for the Rock, Paper, Scissors, Gun Game"""
import random
import time  # Import the time module to add a delay to the game.


def main():
    """Main function for the game"""
    Menu().draw()
    choice = input("\nEnter your choice >>> ")
    match choice:
        case "1":
            while True:
                rounds = int(input("Best of rounds to play? "))
                if rounds % 2 == 0:
                    print("Please enter an odd number")
                    continue
                else:
                    Game().play(rounds)
                    break    
        case "2": Scoreboard().draw()
        case "3": Credits().draw()
        case "4": Instruction().draw()


class Player:
    """Player Class"""
    def __init__(self):
        self.choice = None
        while self.choice not in ["Rock", "Paper", "Scissors"]:
            print('\nChoose "Rock", "Paper", or "Scissors" to play!')
            self.choice = input("\nEnter your choice >>> ")


class Computer:
    """Computer Class"""
    def __init__(self):
        self.choice = None
        self.choice = random.choices(["Rock", "Paper", "Scissors", "Gun"],
                                     weights=[0.3, 0.3, 0.3, 0.1])[0]


class Game:
    """Game Class"""
    def __init__(self):
        self.switch = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper",
        }

    def play(self, rounds):
        """Play the game"""
        print("\nWelcome to Rock, Paper, Scissors, Gun!")
        best_of_rounds = (rounds//2) + 1
        gamecount = 0
        wincount = 0
        tiecount = 0
        losecount = 0
        deathcount = 0

        while (wincount or losecount) < best_of_rounds:
            gamecount += 1
            player = Player().choice
            computer = Computer().choice
            print(f"Computer chose: {computer}!")
            time.sleep(1)

            # Game Logic #
            # If the player and computer chose the same thing, it's a tie.
            if player == computer:
                print("It's a tie!")
                tiecount += 1

            # If the computer chose gun, the player has to roll the dice.
            elif computer == "Gun":
                print("The computer chose gun! " +
                          "Roll the dice to see if you survive! ")

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

                if dice >= 4 and player == "Scissors":
                    print("You cut the gun in half and survived!")
                    print("You win!")
                    wincount += 1

                elif dice >= 4 and player == "Rock":
                    print("You smashed the gun and survived!")
                    print("You win!")
                    wincount += 1

                elif dice >= 4 and player == "Paper":
                    print("You pushed the paper into " +
                              "the gun and survived!")
                    print("You win!")
                    wincount += 1

                else:
                    print("You died! Better luck next time.")
                    deathcount += 1

            # If the player chose the losing choice, they lose.
            elif player == self.switch[computer]:
                print("You lose!")
                losecount += 1

            # If the player chose the winning choice, they win.
            else:
                print("You win!")
                wincount += 1

            if wincount == best_of_rounds or losecount == best_of_rounds:
                print("We have a winner")
                if wincount == best_of_rounds:
                    print("And it's the user")
                elif losecount == best_of_rounds:
                    print("And it's the computer")
                rematch = input("Wanna play again? , yes/no: ")

                if rematch == "no":
                    print("Good game :)")
            
                    # Game stats #
                    print("\nLatest score:")
                    print(f"Game count: {gamecount}")
                    time.sleep(0.5)
                    print(f"Win count: {wincount}")
                    time.sleep(0.5)
                    print(f"Tie count: {tiecount}")
                    time.sleep(0.5)
                    print(f"Lose count: {losecount}")
                    time.sleep(0.5)
                    print(f"Death count: {deathcount}")
                    time.sleep(0.5)
                
                elif rematch == "yes":
                    print("reset count")
                    gamecount = 0
                    wincount = 0
                    tiecount = 0
                    losecount = 0
                    deathcount = 0

class Menu:
    """Menu Class"""
    def draw(self):
        """Draws the game menu"""
        print("-----------------------------------")
        print("|*Rock, Paper, Scissors, Gun Game*|")
        print("|---------------------------------|")
        print("| 1. Start Game                   |")
        print("| 2. Scoreboard                   |")
        print("| 3. Exit                         |")
        print("| 4. Instructions                 |")
        print("-----------------------------------")

class Instruction:
    "Instruction Class"
    def draw(self):
        "Draws the game Instruction"
        print("""
              How to Play the game step by step:
              1. The game is Simple and it's about Rock,Papper, Scissors and Gun.
              2. If you have played this game before skip this tutorial, otherwise continue.
              3. To Start, the player choses how many rounds to play.
              4. Then the player will go up agains a computer bot.
              5. The player then has the options Rock, Paper or Scissors
              6. The computer has the options Rock, Paper, Scissors or Gun.
              7. Which ever hand is stronger that person will Win.
              8. Then we do a reapet from 7 to the best of rounds.
              9. The score will show up and show you the results at the end of the rounds.
              10. You could either beat the computer, lose agains the computer or play again.

              
              """)

class Scoreboard:
    """Scoreboard Class"""
    score = 0

    def draw(self):
        """Draws the game scoreboard"""
        print("Scoreboard")
        print(f"Score: {self.score}")


class Credits:
    """Credits Class"""

    def draw(self):
        """Draws the game credits and authors"""
        author1 = "Ngoc Hong (Mi)"
        author2 = "Chris Lubert"
        author3 = "Daniel Jönsson"
        print("-----------------------------------")
        print("|           *Credits*             |")
        print("|---------------------------------|")
        print("|© HKR 2024 - All rights reserved.|")
        print("|---------------------------------|")
        print("|          Created by:            |")
        print(f"|-{author1}                  |")
        print(f"|-{author2}                    |")
        print(f"|-{author3}                  |")
        print("-----------------------------------")
        print("Thank you for playing!")


if __name__ == "__main__":
    main()
