"""
Program: Bicycle.py
Author: Tony Ehlert
Last date modified: 4/7/2023

The purpose of this program is to create a Bicycle class derived from the Rider class
The input is the required data needed to create and test objects created
The output is none
"""
from Topic3.Rider import Rider


class Bicycle(Rider):
    """Bicycle class implements abstract class Rider"""
    def __init__(self, type):
        self._type = type

    def ride(self):
        return "Human powered, not enclosed"

    def riders(self):
        return "1 or 2 if tandem or a daredevil"

    @property
    def type(self):
        return self._type

    @type.setter
    def set_type(self, type):
        self.self._type = type

    def __str__(self):
        return "Bicycle(Type: " + self._type + ")"

    def __repr__(self):
        return "Bicycle(\"" + self._type + "\")"


# driver/main()
if __name__ == "__main__":
    # create Bicycle object
    road_bike = Bicycle("Road Bike")

    # call __str__ and __repr__ methods
    print(road_bike)
    print(road_bike.__repr__())

    # call and print abstract methods
    print(road_bike.ride())
    print(road_bike.riders())

    # garbage collection
    del road_bike