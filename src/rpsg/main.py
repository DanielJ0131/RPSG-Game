"""This is the main file for the Rock, Paper, Scissors, Gun Game."""

# Import the other modules.
from game import Game
from menu import Menu
from instructions import Instruction
from scoreboard import Scoreboard
from credits import Credits
#Just a test text --------------------------->

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
                    if answer in ["yes", "y"]:
                        lst.append(player_name)
                        break
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


if __name__ == "__main__":
    main()
