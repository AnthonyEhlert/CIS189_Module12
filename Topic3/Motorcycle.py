"""
Program: Bicycle.py
Author: Tony Ehlert
Last date modified: 4/7/2023

The purpose of this program is to create a Motorcycle class derived from the Rider class
The input is the required data needed to create and test objects created
The output is none
"""
from Topic3.Rider import Rider


class Motorcycle(Rider):
    """Motorcycle class implements abstract class Rider"""

    def __init__(self, brand):
        self._brand = brand

    def ride(self):
        return "Engine powered, not enclosed"

    def riders(self):
        return "1 or 2"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def set_brand(self, brand):
        self.self._brand = brand

    def __str__(self):
        return "Motorcycle(Brand: " + self._brand + ")"

    def __repr__(self):
        return "Motorcycle(\"" + self._brand + "\")"

# driver/main()
if __name__ == "__main__":
    # create Motorcycle object
    harley_motorcycle = Motorcycle("Harley Davidson")

    # call __str__ and __repr__ methods
    print(harley_motorcycle)
    print(harley_motorcycle.__repr__())

    # call and print abstract methods
    print(harley_motorcycle.ride())
    print(harley_motorcycle.riders())

    # garbage collection
    del harley_motorcycle