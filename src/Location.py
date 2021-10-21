# MacOS
# -*- coding: UTF-8 -*-
# Python 3
"""
Zweck der Datei: Implementierung der Hilfklasse Location.

Autorin: Daryna Ivanova
Datum: 02.09.21
"""


class Location():
    """
    An auxiliary class to implement changes in character's location.

    Attributes
    ----------
    current_location : str
        Current location of the character.

    Methods
    -------
    change_location()
        Changes current location of the character.
    """

    def __init__(self, current_location: str):
        """
        Parameters
        ----------
        current_location : str
            Current location of the Character(), given as a string.
        """
        self.current_location = current_location

    def change_location(self, new_location: str):
        """
        Change current location of the character to the given one.

        Parameters
        ----------
        new_location : str
            Name of the new location.
        """
        self.current_location = new_location
