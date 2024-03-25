# Rock, Paper or Scissors game - Examination2 

By Ngoc Hong (Mi), Chris Lubert and Daniel Jönsson

This is a Python implementation of the game Rock, Paper or Scissors. This game is designed to play in the terminal. It's fun and entertaining.

## Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#Installation)
- [Usage](#usage)
- [Rules for the game](#rules-for-the-game)
- [How to contribute to the project](#How-to-contribute-to-the-project) 
- [How to generate Documentation and UML diagrams](#How-to-generate-documentation-and-UML-diagrams)



## Introduction
For those who love Rock, Paper, Scissors with a twist. The game includes having a gun and there is a surprise on what will happen if we chose gun or if the computer chose gun. There can only be a winner, it's either the computer, the user or one of the users when playing 2v2. The object is to win best of 5 rounds. The first one who gets to 5 wins first is the winner. Your score is saved and you can either play again or quit the game.

There are instruction in the game on how to play and this guide is to help with the setup procces for being able to run the game. Also some guidance about other funcionalities.


## Rules for the game
The game implemented is called Rock, paper and Scissors. It's a decision and a dice game that is simple to play, but we added a twist to the game. You can read more about how the basic Rock, paper and Scissors game works on https://en.wikipedia.org/wiki/Rock_paper_scissors


## Requirements
- A package manager (brew for MacOS and Chocolatey for Windows):
    - How to install brew for MacOS is in this source https://brew.sh/
    - How to install Chocolatey for Windows is in this source https://docs.chocolatey.org/en-us/choco/setup
- A Python interpreter with at least version 3.3.
    - Open the terminal to check if you have installed python and the right version.
```bash
python --version 
python3 --version
```
- To install the latest pytho using package manager (Brew or Chocolatey) in the terminal.
```bash
brew install python #for Mac
choco install python #for Windows
```
- You have to conect to the Wifi for downloading this source code.
- More about Git Bash is found in https://git-scm.com/downloads.
- If you you do not have make tools, which is used to compile the source code of the program and it installs it on the system.
To install it:
```bash
brew install python #for Mac
choco install make  #for Windows
```

- To use our UML diagrams from our code. You need to install Graphviz package:
```bash
brew install graphviz #for Mac
choco install graphviz #for Windows
```

## Installation
To run the Rock,Paper and Scissors game, you need to follow these steps bellow:

### First step:
Clone the git repository to your local machine using the terminal provided by git Bash:
```bash
git clone git@github.com:DanielJ0131/Examination2.git
```
The repository and the source code contains all the Python files for executing the game. There are also other files for testing and different functionalities.

### Second step:
Navigate to the project directory usually found in the home folder. Open a new terminal at the root folder `Examination2`.

### Third step:
Vitual enviroment needs to be created nad activated by running these commands:
```bash
make venv
. .venv/bin/activate #for Mac
. .venv/Scripts/activate #for Windows
```
### Fourth step:
Install dependencies specified in the requirement.txt file with the command:
```bash 
make install
```

To see if it is installed, type in command:
```bash
make installed
``` 

To exit the virtual enviroment, type in command:
```bash
deactivate
```


## How to generate Documentation and UML diagrams


### Download Class & Package UML Diagram in terminal for Windows & Mac OS/ Linux
**Do everything in virtual enviroment by installing venv!**
**Follow these steps below!**

**Step: 1** Installing venv
1. Open Directory in Terminal, write (cd Examination2)
2. Create the virtual environment with help of our given
3. Makefile. In the Terminal, write (python3 -m venv .venv) and (make venv)
4. Activate the venv, write for Windows (. .venv/Scripts/activate) and for Mac/Linux (. .venv/bin/activate)
4. Install the virtual packages in venv. write (make install)
5. Check the installed virtual packages (make installed)

**Step: 2**
Install the dot command to help generating the UML pictures from source code structure. 
1. choco install graphviz (Window) / brew install graphviz (Mac OS/ Linux)
2. dot -V (to check what version, optional!)

**Step: 3**
After virtuel enviroment is opened and graphviz is installed open up rpsg map is necessary in Examination2.
1. cd Examination2 (if not already opened)
2. cd src
3. cd rpsg
* Should look something like this in the terminal ~/Examination2/src/rpsg

**Step: 4**
1. make pyreverse
* And now UML diagram is installed.