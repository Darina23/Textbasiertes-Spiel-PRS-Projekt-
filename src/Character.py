# MacOS
# -*- coding: UTF-8 -*-
# Python 3
"""
Zweck der Datei: Implementierung der Spielbefehlen.

Autorin: Daryna Ivanova
Datum: 07.09.21
"""


import sys
import time
import random
import textwrap
from src.Scenes import Scenes
from src.Location import Location
from src.FirstRiddle import FirstRiddle
from src.SecondRiddle import SecondRiddle


class Character():
    """
    A class to implement game commands.

    Attributes
    ----------
    current_location : str
        Current location of a character, changed to the initialised object of
        a class Location.
    bag : dict
        Consists of the possessed objects. At the beginning of the game the
        character has only 20 euros. A train ticket and a book can be also
        added in the course of the game.
    logic_dict : dict
        A dictionary with the locations as keys and possible actions according
        to the location. Needed for implementation of commands.
    time_for_riddle : None
        After executing FirstRiddle().riddle(), the object's attribute will be
        taken over. The value will be changed to int.

    Methods
    -------
    quit_game()
        Quits the game. Can be invoked at any time during the game.
    end()
         Asks whether the game should be restarted or quitted. Will be
         automatically invoked in the end of the game.
    inspect_bag()
        Shows the content of the character's bag. Can be invoked at any time
        during the game.
    get_train()
        Depending on time used to solve the first riddle, decides which train
        will be taken (first/second train). Will be invoked if the character
        has a train ticket and current location is either Potsdam Hbf or
        Ticket machine.
    buy_ticket()
        Changes value of self.bag["ticket"] to True and, subtracts 5 euro from
        self.bag["money"] after the riddle was solved. The time needed for
        guessing will be saved in self.time_for_riddle.
    get_to_golm()
        Depending on the current location, the next location will be canged.
    show_ticket()
        Changes location either to "Fee payment" or "Library" with the 50%
        chance.
    pay_fee()
        Subtracts 15 euro from self.bag["money"] and changes location to
        "Library".
    get_coffee()
        Print a sentence, depending of whether the coffee is affordable or not
        and the game will end.
    read_book()
        Prints the scene description and ends the game.
    at_the_library()
        Executes the scene at the Library, including the second riddle and adds
        the book to the character's bag. An auxilliary method.
    get_message()
        Returns a standard message for the case, when an entered command is
        not acceptable for the current location.
    act()
        Invokes the appropriate method corresponding to user's input.
    """

    def __init__(self, current_location: str):
        """
        Parameters
        ----------
        current_location : str
            Current location of the character. Starting position should be
            "Potsdam Hbf". It will be then changed to the object of a class
            Location with the attribute "current_location" and a method
            "change_location".
        bag : dict
            A dict, consisting of the objects, possessed by the character. The
            keys are the namings of the objects and the values are their state.
            At the beginning there will be only 20 euros (represented as int).
            The contents will be changed during the game. It can consist of
            "money": int, "ticket": bool and "book": bool.
        logic_dict : dict
            A dictionary with the locations as keys and possible actions
            according to the current_location.
            Needed for commands implementation.
        time_for_riddle : None
            After the execution of the FirstRiddle().riddle() the time needed
            to solve the riddle will be saved as int.
        """

        self.current_location = Location(current_location)
        self.bag = {"money": 20, "ticket": False, "book": False}
        # logical steps with the possible actions
        self.logic_dict = {"Potsdam Hbf": ["inspect bag", "buy ticket",
                                           "exit"],
                           "Ticket machine": ["inspect bag", "get train",
                                              "exit"],
                           "First train": ["inspect bag", "get to golm",
                                           "exit"],
                           "Second train": ["inspect bag", "get to golm",
                                            "exit"],
                           "Ticket control": ["inspect bag", "show ticket",
                                              "exit"],
                           "Fee payment": ["inspect bag", "pay fee", "exit"],
                           "Library": ["inspect bag", "get coffee",
                                       "read book", "exit"]}
        self.time_for_riddle = None

    def quit_game(self):
        """Quit the game."""
        print("\nThank you for playing. Bye!\n")
        sys.exit()

    def end(self):
        """Ask whether the game should be restarted or quitted."""
        print("\nThe game is over.",
              "Do you want to quit (Q/q) or restart (R/r) the game?")
        ask = input("\n\u23E9 ")
        if ask.lower() == "q":
            self.quit_game()
        elif ask.lower() == "r":
            self.bag = {"money": 20, "ticket": False, "book": False}
            self.time_for_riddle = None
            print("\n")
            Scenes("Introduction.txt")
            self.current_location.change_location("Potsdam Hbf")
            time.sleep(10)
            print("\n### POTSDAM HBF ###")
            Scenes("Potsdam_Hbf.txt")
        else:
            print("\nPlease, write 'Q/q' or 'R/r'.\n")

    def inspect_bag(self):
        """Print out the content of the character's bag."""
        money = "{} euros".format(self.bag["money"])
        if self.bag["ticket"] == True or self.bag["book"] == True:
            if self.bag["book"] == False:
                print("\nYou have", money, "and a train ticket.\n")
            else:
                print("\nYou have", money, ", a train ticket and a book.\n")
        else:
            print("\nYou have {}.\n".format(money))

    def get_train(self):
        """
        Check the time spent to solve the riddle and change the location to
        "First train" or "Second train".
        """
        if self.bag["ticket"] == False:
            print("\nYou cannot do it without a valid ticket!",
                  "Go buy the ticket first.\n")
        elif self.current_location.current_location not in ["Potsdam Hbf",
                                                            "Ticket machine"]:
            print(self.get_message())
        else:
            if self.time_for_riddle <= 120:
                self.current_location.change_location("First train")
                print("\n### FIRST TRAIN ###")
                Scenes("First_train.txt")
            else:
                self.current_location.change_location("Second train")
                print("\n### SECOND TRAIN ###")
                Scenes("Second_train.txt")

    def buy_ticket(self):
        """
        Save the time used for the first riddle and change the content of
        self.bag.
        """
        if self.current_location.current_location == "Potsdam Hbf" \
                and self.bag["ticket"] == False:
            print("\n### TICKET MACHINE ###")
            Scenes("Ticket_machine.txt")
            time.sleep(20)
            first_r = FirstRiddle()
            first_r.riddle()
            self.current_location.change_location("Ticket machine")
            if first_r.ticket == True:
                self.bag["ticket"] = True
                self.bag["money"] -= 5
                print("\nHurraah! You got the ticket!\n")
                self.time_for_riddle = first_r.time
        elif self.current_location.current_location == "Ticket machine" \
                and self.bag["ticket"] == True:
            print("\nYou already have a ticket!\n")
        else:
            print(self.get_message())

    def get_to_golm(self):
        """
        Decide which location will be selected next, according to the current
        location.
        """
        if self.current_location.current_location == "First train":
            if random.random() > 0.40:
                self.current_location.change_location("Ticket control")
                print("\n### TICKET CONTROL ###")
                Scenes("Ticket_control.txt")
            else:
                self.at_the_library()
        elif self.current_location.current_location == "Second train":
            self.current_location.change_location("Library")
            Scenes("End.txt")
        else:
            print(self.get_message())

    def show_ticket(self):
        """Decide randomly if the fine should be paid."""
        if self.current_location.current_location == "Ticket control":
            if random.random() > 0.50:
                self.current_location.change_location("Fee payment")
                Scenes("Fee_payment.txt")
            else:
                Scenes("No_fee_payment.txt")
                time.sleep(10)
                self.at_the_library()
        else:
            print(self.get_message())

    def pay_fee(self):
        """
        Subtract 15 euros from self.bag["money"] and execute the Library-scene.
        """
        if self.current_location.current_location == "Fee payment":
            self.bag["money"] -= 15
            print("\nNow you oficially have no money for coffee.",
                  "Could this day be more terrible???\n")
            time.sleep(3)
            self.at_the_library()
        else:
            print(self.get_message())

    def get_coffee(self):
        """
        Print a sentence, depending of whether the coffee is affordable or not
        and end the game.
        """
        if self.current_location.current_location == "Library":
            if self.bag["money"] != None and self.bag["money"] > 0:
                print("\n\u2615",
                      "Well, everything gets better with coffee, isn't it?",
                      "\n")
                self.end()
            else:
                print("\nSorry, you have no money left.\n")
        elif self.current_location.current_location == "Second train":
            print("\n",
                  "Phew, at least you can enjoy this cup of coffee \u2615...",
                  "\n")
            self.end()
        else:
            print(self.get_message())

    def read_book(self):
        """Print the scene description and end the game."""
        if self.current_location.current_location == "Library":
            if self.bag["book"] == True:
                print("\n")
                Scenes("Happy_end.txt")
                self.end()
            else:
                print("\nYou don't have any book.\n")
        else:
            print(self.get_message())

    def at_the_library(self):
        """
        Execute the scene at the Library, including the second riddle and add
        the book to the character's bag.
        """
        print("\n### LIBRARY ###")
        Scenes("Library.txt")
        time.sleep(15)
        second_r = SecondRiddle()
        second_r.riddle()
        self.current_location.change_location("Library")
        if second_r.book == True:
            self.bag["book"] = True
            Scenes("Library_riddle.txt")

    def get_message(self) -> str:
        """
        Generate a standard message.

        Returns
        -------
        message : str
             A standard messsage for the case, when an entered command is
             not acceptable for the current location of the character.

        """
        text = ("\n" + "You can't do it here, but here are the actions "
                "you can do: " + str(self.logic_dict.get(
                    self.current_location.current_location)))
        message = textwrap.fill(text)
        return message

    def act(self, action: str):
        """
        Execute the command.

        Parameters
        ----------
        action : str
            User's input, a command.

        Returns
        -------
        Invokes the corresponding method.

        """
        act = str(action.lower())
        actions_list = sorted({x for v in self.logic_dict.values() for x in v})
        if act in actions_list:
            if act == "inspect bag":
                self.inspect_bag()
            elif act == "exit":
                self.quit_game()
            elif act == "get train":
                self.get_train()
            elif act == "buy ticket":
                self.buy_ticket()
            elif act == "get to golm":
                self.get_to_golm()
            elif act == "show ticket":
                self.show_ticket()
            elif act == "pay fee":
                self.pay_fee(),
            elif act == "get coffee":
                self.get_coffee()
            elif act == "read book":
                self.read_book()
        else:
            print("\nOops, I don't understand this command.\n")
