"""This is the main file for the Rock, Paper, Scissors, Gun Game"""

""" I have fixed the code from bug, märker också att det är andra konstigheter med koden som Gamestats dycker upp hela tiden i Terminalen när det är en tie, men annars jätte bra skriven kod //Chris """
import random
import time


class Player:
    """Player Class"""
    def __init__(self):
        self.player = None
    choice = input("Enter your choice >>> ")


class Computer:
    """Computer Class"""
    def __init__(self):
        self.computer = None
    choice = random.choices(["Rock", "Paper", "Scissors", "Gun"],
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
    while True:
        gamecount = 0
        wincount = 0
        tiecount = 0
        losecount = 0

        while True:
            gamecount += 1
            player = Player()
            computer = Computer()
            print(f"Computer chose: {computer.choice}!")
            time.sleep(1)

            # Game Logic #
            # If the player and computer chose the same thing, it's a tie.
            if player.choice == computer.choice:
                print("It's a tie!")
                tiecount += 1
                break

            # If the computer chose gun, the player has to roll the dice.
            elif computer.choice == "Gun":
                print("The computer chose gun!" +
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

                if dice >= 3 and player.choice == "Scissors":
                    print("You cut the gun in half and survived!")
                    wincount += 1

                elif dice >= 3 and player.choice == "Rock":
                    print("You smashed the gun and survived!")
                    wincount += 1

                elif dice >= 3 and player.choice == "Paper":
                    print("You pushed the paper into the gun and survived!")
                    wincount += 1

                else:
                    print("You died! Better luck next time.")
                    losecount += 1
                    death = True

            # If the player chose the winning choice, they win.
            elif player.choice == self.switch[computer.choice]:
                print("You win!")
                wincount += 1

            # If the player chose the losing choice, they lose.
            else:
                print("You lost!")
                losecount += 1

        # Game Stats #
        print(f"\nGame count: {gamecount}")
        print(f"Win count: {wincount}")
        print(f"Tie count: {tiecount}")
        print(f"Lose count: {losecount}")


if __name__ == "__main__":
    Game().play()
