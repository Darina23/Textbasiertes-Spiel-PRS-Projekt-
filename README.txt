######################################
       INTERACTIVE FICTION GAME
######################################


A readme file for a command-line game implementation.


# Program Description #
-----------------------

A text adventure game, also known as interactive fiction.

The player has to interact with the different scene descriptions during the game, to get a book from the Golm's library. Depending on the choices the user makes and the time he spends on some tasks, the game may take different directions, and therefore different endings.


# Installation - relevant information #
----------------------------

- 'animals.csv' file has to be located in the main directory, together with 'src/', 'Scenes/' and 'main.py';

- 'Scenes/' contains txt files with scene descriptions;

- 'src/' consists of separate classes with the game's logic;

- 'main.py' is needed for the program execution;


# Program execution #
---------------------

-> In a terminal enter a path to the main directory, where main.py and other data is saved.

  #############   
###   Run:   ###    >>> python3 main.py 
  ############                   
                          
=> After that a scene will be shown and you'll have to enter the action you want to do next;

=> Here are all the actions you can do:   "inspect bag", "buy ticket", "exit", "get train", "get to golm", 					"show ticket", "pay fee", "get coffee", "read book";

=> Each scene has a list of acceptable actions, so that every time you enter an inappropriate one, you'll get the hint.

=> The Riddles can be skipped by entering "###".

=> You can check your bag or exit the game any time while playing.


-> In the end of the game you will be asked whether you want to quit or restart the game.

---------------------