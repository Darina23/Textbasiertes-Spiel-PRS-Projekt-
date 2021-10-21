# MacOS
# -*- coding: UTF-8 -*-
# Python 3
"""
Zweck der Datei: Programmausführung.

Autorin: Daryna Ivanova
Datum: 20.09.21
"""


import time
from src.Scenes import Scenes
from src.Character import Character


def main():
    """Execute the program."""
    Scenes("Introduction.txt")
    time.sleep(15)
    print("### POTSDAM HBF ###")
    Scenes("Potsdam_Hbf.txt")
    char = Character("Potsdam Hbf")
    while True:
        action = input("\nWhat do you want to do?\n\u23E9 ")
        char.act(action)


if __name__ == "__main__":
    main()
