"""This is the main file for the Rock, Paper, Scissors, Gun Game."""

# pylint: disable=import-error
# Import the other modules.
import time
from game import Game
from menu import Menu
from instructions import Instructions
from scoreboard import Scoreboard
from credits import Credits
from player import Player
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


def main():
    """Use the main function."""
    player = Player()
    while True:
        Menu().draw()
        choice = input(Fore.LIGHTWHITE_EX + Style.BRIGHT +
                       "\nEnter your choice >>> ")
        match choice:
            case "1":
                player.input_name()
                rounds = 9
                Game().play(rounds, player)
                continue
            case "2":
                Scoreboard().draw()
                time.sleep(5)
                continue
            case "3":
                Instructions().draw()
                time.sleep(5)
                continue
            case "4":
                Credits().draw()
                break


if __name__ == "__main__":
    main()
