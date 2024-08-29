Usage
=====

.. _installation:

Installation
------------

To use RPSG-Game, first install it using pip.
We also have an alternative, git clone:

.. code-block:: console

.. autofunction::
   pip install virtualenv
   virtualenv venv
   source venv/bin/activate
   (.venv) $ pip install git@github.com:DanielJ0131/RPSG-Game.git
   (.venv) $ git clone git@github.com:DanielJ0131/RPSG-Game.git


Starting the Game
----------------

To start the Game,
Use the cd (Change directory) command to navigate to the directory where your Python script is located.
Like a folder called ``cd path/to/RPSG-Game``: 

.. autofunction:: cd RPSG-Game

To Run the python script use "python main.py" to start the game. 

.. autoexception:: python main.py

For example:
>>> pip install virtualenv
>>> virtualenv venv
>>> source venv/bin/activate

>>> pip install RPSG-Game
>>> cd path/to/RPSG-Game
>>> python main.py 
>>> 
   ===================================
   |         Welcome to the           |
   |  * Rock, Paper, Scissors, Gun *  |
   |              Game!               |
   |==================================|
   | 1. Start Game                    |
   | 2. Scoreboard                    |
   | 3. Instructions                  |
   | 4. Credits                       |
   |==================================|


