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


def main():
    """Use the main function."""
    game = Game()
    player = Player()
    while True:
        Menu().draw()
        choice = input("\nEnter your choice >>> ")
        match choice:
            case "1":
                game_mode = None
                while game_mode not in ["player", "computer"]:
                    game_mode = input('Enter mode "player"' +
                                      ' or "computer": ').lower()
                rounds = 9
                if game_mode == "player":
                    player1 = Player()
                    player2 = Player()
                    print("(Player one)")
                    player1.input_name()
                    print("(Player two)")
                    player2.input_name()
                    game.play_pvp(rounds, player1, player2)
                    continue

                player.input_name()
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
