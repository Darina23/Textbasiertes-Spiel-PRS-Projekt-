# MacOS
# -*- coding: UTF-8 -*-
# Python 3
"""
Zweck der Datei: Einlesen der Szenenbeschreibungen.

Autorin: Daryna Ivanova
Datum: 02.09.21
"""


import os
import textwrap


class Scenes():
    """
    A class to read and show txt-files with scene descriptions.

    Attributes
    ----------
    txt_name: str
        Name of the file to be read.
    """

    def __init__(self, txt_name: str):
        # path to the scene text
        scene_txt = os.getcwd() + "/Scenes/" + txt_name
        with open(scene_txt, "r", encoding="utf-8", errors="ignore") as f:
            read = textwrap.fill(f.read())
            print("\n", read, "\n")
