"""
Program: Rider.py
Author: Tony Ehlert
Last date modified: 4/7/2023

The purpose of this program is to create an abstract Rider class
The input is the required data needed to create the class
The output is none
"""
from abc import ABC, abstractmethod


class Rider(ABC):
    """Abstract Rider Class"""

    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def riders(self):
        pass
