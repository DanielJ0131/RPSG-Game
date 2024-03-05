"""Menu Module."""
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


class Menu:
    """Menu Class."""

    def draw(self):
        """Draws the game menu."""
        menu_items = [
            "Start Game",
            "Scoreboard",
            "Instructions",
            "Credits"
        ]

        print(
            f"{Fore.LIGHTYELLOW_EX} ==================================\n"
            f"|         {Fore.MAGENTA}Welcome to the " +
            f"{Fore.LIGHTYELLOW_EX:<15}|\n"
            f"|  * {Fore.RED}Rock, {Fore.BLUE}Paper, {Fore.YELLOW}Scissors," +
            f"{Fore.GREEN}Gun {Fore.LIGHTYELLOW_EX}*   |\n"
            f"|              {Fore.MAGENTA}Game!{Fore.LIGHTYELLOW_EX:<20}|\n"
            f"|==================================|"
        )

        for i, item in enumerate(menu_items, start=1):
            print(
                f"{Fore.LIGHTYELLOW_EX}| {i}. {Fore.LIGHTWHITE_EX}" +
                f"{Style.BRIGHT}" +
                f"{item:<28} {Fore.LIGHTYELLOW_EX} |"
            )

        print(f"{Fore.LIGHTYELLOW_EX} ==================================")

    def __str__(self):
        """Return the class name."""
        return "Menu"
