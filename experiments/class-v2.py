#!/usr/bin/python3

class Car:
    # class variable
    wheels = 4

    def __init__(self):
        # instance variables
        self.mil = 10
        self.com = "Renault"


c1 = Car()

c1.mil = 8

c2 = Car()

Car.wheels = 5

print(f"{c1.mil}, {c1.com}, {c1.wheels}")

print(f"{c2.mil}, {c2.com}, {c2.wheels}")
