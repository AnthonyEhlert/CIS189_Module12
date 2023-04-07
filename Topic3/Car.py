"""
Program: Car.py
Author: Tony Ehlert
Last date modified: 4/7/2023

The purpose of this program is to create a Car class derived from the Rider class
The input is the required data needed to create and test objects created
The output is none
"""
from Topic3.Rider import Rider


class Car(Rider):
    """Car class implements abstract class Rider"""

    def __init__(self, make, model):
        self._make = make
        self._model = model

    def ride(self):
        return "Engine powered, enclosed"

    def riders(self):
        return "1 plus comfortably"

    @property
    def make(self):
        return self._make

    @make.setter
    def set_make(self, make):
        self.self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def set_model(self, model):
        self.self._model = model

    def __str__(self):
        return "Car(Make: " + self._make + ", Model: " + self._model + ")"

    def __repr__(self):
        return "Car(\"" + self._make + "\", \"" + self.model + "\")"

# driver/main()
if __name__ == "__main__":
    # create Car object
    outback_car = Car("Subaru", "Outback")

    # call __str__ and __repr__ methods
    print(outback_car)
    print(outback_car.__repr__())

    # call and print abstract methods
    print(outback_car.ride())
    print(outback_car.riders())

    # garbage collection
    del outback_car