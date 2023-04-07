"""
Program: abstract_class_assignment_driver
Author: Tony Ehlert
Last date modified: 4/7/2023

The purpose of this program is to create one object each of three different classes all implementing the
abstract Rider class and call the abstract methods for each object

The input is the required data to create a Bicycle object, Motorcycle object, and Car object

The output is print statements of each object's implemented abstract methods
"""
from Topic3.Bicycle import Bicycle
from Topic3.Car import Car
from Topic3.Motorcycle import Motorcycle

if __name__ == "__main__":
    # create Bicycle object
    road_bike = Bicycle("Road Bike")

    # create Motorcycle object
    harley_motorcycle = Motorcycle("Harley Davidson")

    # create Car object
    outback_car = Car("Subaru", "Outback")

    # call and print Bicycle abstract methods
    print("\nBICYCLE IMPLEMENTED METHODS:")
    print(road_bike.ride())
    print(road_bike.riders())

    # call and print Motorcycle abstract methods
    print("\nMOTORCYCLE IMPLEMENTED METHODS:")
    print(harley_motorcycle.ride())
    print(harley_motorcycle.riders())

    # call and print Car abstract methods
    print("\nCAR IMPLEMENTED METHODS:")
    print(outback_car.ride())
    print(outback_car.riders())

    # garbage collection
    del road_bike
    del harley_motorcycle
    del outback_car
