"""This is the main file for the Rock, Paper, Scissors, Gun Game."""

# Import the other modules.
from game import Game
from menu import Menu
from player import Player
from instructions import Instruction
from scoreboard import Scoreboard
from credits import Credits


def main():
    """Use the main function."""
    player = Player()
    while True:
        Menu().draw()
        choice = input("\nEnter your choice >>> ")
        match choice:
            case "1":
                player.set_name()
                rounds = 9
                Game().play(rounds, player)
                continue
            case "2":
                Scoreboard().draw()
                continue
            case "3":
                Instruction().draw()
                continue
            case "4":
                Credits().draw()
                break


if __name__ == "__main__":
    main()
