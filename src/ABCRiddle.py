# MacOS
# -*- coding: UTF-8 -*-
# Python 3
"""
Zweck der Datei: eine abstrakte Klasse für die Implementierung von Rätsel.

Autorin: Daryna Ivanova
Datum: 10.09.21
"""


from abc import ABC, abstractmethod


class Riddle(ABC):
    """An abstract class for implementation of the riddles."""

    def __init__(self):
        pass

    @abstractmethod
    def random_data(self):
        """Choose random data."""
        pass

    @abstractmethod
    def riddle(self):
        """Implement the riddle."""
        pass
