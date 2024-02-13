"""This is the main file for the Rock, Paper, Scissors, Gun game"""
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
        death = False

        gamecount = 0
        wincount = 0
        tiecount = 0
        losecount = 0

        while death is not True:

            gamecount += 1
            player = Player()
            computer = Computer()
            print(f"Computer chose: {computer.choice}!")
            time.sleep(1)

            if player.choice == computer.choice:
                print("It's a tie!")
                tiecount += 1
                break

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
                    print("You pushed the paper into the gun and !")
                    wincount += 1

                else:
                    print("You died! Better luck next time.")
                    losecount += 1
                    death = True

                break

            elif player.choice == self.switch[computer.choice]:
                print("You win!")
                wincount += 1

            else:
                print("You lost!")
                losecount += 1

        print(f"\nGame count: {gamecount}")
        print(f"Win count: {wincount}")
        print(f"Tie count: {tiecount}")
        print(f"Lose count: {losecount}")


if __name__ == "__main__":
    Game().play()
