# MacOS
# -*- coding: UTF-8 -*-
# Python 3
"""
Zweck der Datei: Implementierung des ersten Rätsels.

Autorin: Daryna Ivanova
Datum: 10.09.21
"""


import time
import nltk
import random
import textwrap
from nltk.tokenize.treebank import TreebankWordDetokenizer
from src.ABCRiddle import Riddle


class FirstRiddle(Riddle):
    """
    A subclass of an abstract class Riddle for the implementation of the first
    riddle (guess a word from 'Alice's Adventures in Wonderland').

    Attributes
    ----------
    alice_sents : list
        List of sentences from 'Alice's Adventures in Wonderland', where each
        sentence is a list of tokens.
    ticket : bool
        The default is False. After solving the riddle will be changed to True.
    time : None
        After solving the riddle will be changed to int, the time used for
        solving the riddle.

    Methods
    -------
    random_data()
        Chooses a random sentence and a word in the sentence. An abstract
        method.
    riddle()
         Executes the riddle. An abstract method.
    """

    def __init__(self):
        """
        Check if the book is successfully downloaded.

        Parameters
        ----------
        alice_sents : list
            List of sentences from 'Alice's Adventures in Wonderland', where
            each sentence is a list of tokens.
        ticket : bool
            The default is False. After solving the riddle will be changed to
            True.
        time : None
            The time used for solving the riddle. Afterwards will be changed
            to integer.
        """
        try:
            self.alice_sents = nltk.corpus.gutenberg.sents("carroll-alice.txt")
        except LookupError:
            print("Check if gutenberg corpus is downloaded.")
        self.ticket = False
        self.time = None

    def random_data(self) -> (str, str):
        """
        Choose a random sentence and a word in the sentence.

        Returns
        -------
        (str, str)
            random_sent : str
                A randomly chosen sentence.
            random_word : str
                A randomly chosen word from the sentence.
        """
        random_sent = random.choice(self.alice_sents)
        # random sentence without punctuation and numbers
        cleaned_sent = [w for w in random_sent if w.isalpha()]
        random_word = random.choice(cleaned_sent)
        pos_tag = nltk.pos_tag([random_word], tagset='universal')
        # replace a random word with the POS-tag
        for index, word in enumerate(random_sent):
            if word == random_word:
                first_occurence = index
        random_sent[first_occurence] = str(pos_tag[0][1])
        random_sent = TreebankWordDetokenizer().detokenize(random_sent)
        return random_sent, random_word

    def riddle(self):
        """Execute the riddle."""
        sent, word = self.random_data()
        chances = 3
        print("\n", textwrap.fill(sent), "\n")
        start_time = time.time()
        while True:
            if input("The answer is: ").lower() in [word.lower(), "###"]:
                self.ticket = True
                end_time = time.time() - start_time
                self.time = int(end_time)
                break
            elif chances == 1:
                sent, word = self.random_data()
                print("\n", textwrap.fill(sent), "\n")
                chances = 3
            else:
                chances -= 1
