"""
CP1404/CP5632 Practical
SilverServiceTaxi class, derived from Taxi
"""
from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi with added fanciness and flagfall."""

    flagfall = 4.50  # A fixed charge added to the fare for each ride

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)  # Initialize the parent class Taxi
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def get_fare(self):
        """Calculate the total fare including the flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation including the flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"