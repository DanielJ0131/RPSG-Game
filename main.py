"""This is the main file for the Rock, Paper, Scissors, Gun Game"""
import random
import time  # Import the time module to add a delay to the game.


def main():
    """Main function to start the game."""
    Game().play()


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

    def play(self):
        """Play the game"""
        print("\nWelcome to Rock, Paper, Scissors, Gun!")
        while True:
            gamecount = 0
            wincount = 0
            tiecount = 0
            losecount = 0

            while True:
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

                    if dice >= 3 and player == "Scissors":
                        print("You cut the gun in half and survived!")
                        wincount += 1

                    elif dice >= 3 and player == "Rock":
                        print("You smashed the gun and survived!")
                        wincount += 1

                    elif dice >= 3 and player == "Paper":
                        print("You pushed the paper into" +
                              "the gun and survived!")
                        wincount += 1

                    else:
                        print("You died! Better luck next time.")
                        losecount += 1

            # If the player chose the losing choice, they lose.
                elif player == self.switch[computer]:
                    print("You lose!")
                    losecount += 1

            # If the player chose the winning choice, they win.
                else:
                    print("You win!")
                    wincount += 1

                # Game stats #
                print(f"\nGame count: {gamecount}")
                time.sleep(0.5)
                print(f"Win count: {wincount}")
                time.sleep(0.5)
                print(f"Tie count: {tiecount}")
                time.sleep(0.5)
                print(f"Lose count: {losecount}")
                time.sleep(0.5)


if __name__ == "__main__":
    main()
