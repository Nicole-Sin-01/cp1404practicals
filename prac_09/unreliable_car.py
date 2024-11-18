"""
CP1404/CP5632 Practical
UnreliableCar class, derived from Car
"""
import random
from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of Car that has a reliability factor when driving."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car, with reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability  # Set the reliability attribute

    def drive(self, distance):
        """Override drive method to drive only if a random number is less than reliability."""
        random_chance = random.randint(0, 100)  # Generate a random number between 0 and 100
        if random_chance >= self.reliability:  # Check if the car is reliable enough to drive
            distance = 0 # Set distance to 0 if the car can't drive

        return super().drive(distance)
