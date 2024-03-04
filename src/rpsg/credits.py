"""Credits Module."""
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

class Credits:
    """Credits Class."""

    def __init__(self):
        """Initialize the Credits class."""

    def draw(self):
        """Draws the game credits and authors."""
        author1 = "Ngoc Hong (Mi)"
        author2 = "Chris Lubert"
        author3 = "Daniel Jönsson"
        print(Fore.LIGHTYELLOW_EX + "===================================")
        print(Fore.LIGHTYELLOW_EX + "|           *" + Fore.MAGENTA + "Credits" + Fore.LIGHTYELLOW_EX + "*             |")
        print(Fore.LIGHTYELLOW_EX + "===================================")
        print(Fore.LIGHTYELLOW_EX + "|" + Fore.MAGENTA + "© HKR 2024 - All rights reserved." + Fore.LIGHTYELLOW_EX + "|")
        print(Fore.LIGHTYELLOW_EX + "===================================")
        print(Fore.LIGHTYELLOW_EX + "|          " + Fore.MAGENTA+ "Created by:" + Fore.LIGHTYELLOW_EX +  "            |")
        print(Fore.LIGHTYELLOW_EX + f"|-{author1}                  |")
        print(Fore.LIGHTYELLOW_EX + f"|-{author2}                    |")
        print(Fore.LIGHTYELLOW_EX + f"|-{author3}                  |")
        print(Fore.LIGHTYELLOW_EX + "===================================")
        print(Style.BRIGHT + Fore.MAGENTA + "Thank you for playing!")

    def __str__(self):
        """Return the name of the class."""
        return "Credits"
