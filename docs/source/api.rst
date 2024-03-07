API
===

.. autosummary::
   :About: Our program is structured using various classes, each contained within seperate python files. These classes are designed to manage destinct functionalities
   critical to the program's overall operation. To leverage these functionalities we import the required class from it's corresponding file. For instance the "computer.py"
   file houses a class named 'Computer', which encapsulates logic for generating computer choices in a game, allowing it to compete against a player. Whenever we need to access a specific function, such as the computer choice in Computer class, we call it directly from this class. Consider the "player.py" file, which contains various functions dedicated to the player's interactions within the game. These functions are designed to specifically influence the player's actions and attributes, without affecting other classes or components of the game. This design principle highlights the purpose of using different classes. By doing so, it organizes code around distinct features or behaviors, facilitating easier management, scalability and reusability of code. This approach not only enchances the clarity and efficiency of the codebase but also ensures that modifications in one class do not inadvertently impact other parts of the application. 

   Our project comprises several key python files, including 'main.py',"game.py","computer.py" among others. The 'main.py' file acts as the entry point where all other components
   are orchestrated, ensuring a cohesive run-time environment. Furthermore, we employ various methods to enhance user interaction and data processing. One notable method is the lowercase
   method, which is used to ensure user input is case-insensitive, to prevent errors.

   In summary, our programs's architecture is modular, with each class representing a specific aspect of the program's functionalitiy. This structure not only simplifies code management
   and maintenance, but also facillitates the addtion of new features or modifications to existing ones. So Examination2
   provides a clearer and most structured explanation of the program's design and functionalitiy.
