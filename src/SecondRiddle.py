# MacOS
# -*- coding: UTF-8 -*-
# Python 3
"""
Zweck der Datei: Implementierung des zweiten Rätsels.

Autorin: Daryna Ivanova
Datum: 16.09.21
"""


import os
import csv
import random
import textwrap
from nltk.corpus import wordnet as wn
from src.ABCRiddle import Riddle


class SecondRiddle(Riddle):
    """
    A subclass of an abstract class Riddle for the implementation of the second
    riddle (guess an animal by its definition).

    Attributes
    ----------
    animals_list : list
        List of animals from the animals.csv file.
    book : None
        At first is None. After solving the riddle will be changed to True.

    Methods
    -------
    random_data()
        Chooses a random animal and finds its definition in WordNet.
        An abstract method.
    riddle()
         Executes the riddle. After solving changes self.book to True.
         An abstract method.
    """

    def __init__(self):
        """
        Check if the csv-file can be opened and save its contents to the list.

        Parameters
        ----------
        animals_list : list
            List of animals from the animals.csv file.
        book : None
            At first is None. After solving the riddle will be changed to True.
        """
        self.animals_list = []
        self.book = None
        try:
            with open(os.getcwd() + '/animals.csv', 'r') as f:
                read_file = csv.reader(f)
                for row in read_file:
                    self.animals_list += row
        except LookupError:
            print("Check if 'animals.csv' file is in the main directory.")

    def random_data(self) -> (str, str):
        """
        Choose a random animal and find its definition in WordNet.

        Returns
        -------
        (str, str)
            random_animal : str
                A random animal.
            definition : str
                Definition of a random animal.
        """
        random_animal = random.choice(self.animals_list)
        synsets = wn.synsets(str(random_animal))
        definition = ""
        while True:
            if len(synsets) != 0:
                for synset in synsets:
                    if synset.lexname() == 'noun.animal':
                        definition = synset.definition()
                break
            else:
                random_animal = random.choice(self.animals_list)
                synsets = wn.synsets(str(random_animal))
        return random_animal, definition

    def riddle(self):
        """Execute the riddle."""
        animal, definition = self.random_data()
        print("\n", textwrap.fill(definition), "\n")
        chances = 3
        while True:
            if input("The answer is: ").lower() in [animal, "###"]:
                self.book = True
                break
            elif chances == 1:
                print("\nThe right answer is: ", str(animal), "\n")
                animal, definition = self.random_data()
                print("\n", textwrap.fill(definition), "\n")
                chances = 3
            else:
                chances -= 1
