"""
CP1404/CP5632 Practical
Guitar Class
Estimate: 7 minutes
Actual:

Define the following methods:
__init__ - with defaults name="", year=0, cost=0

__str__ - which uses {} string formatting to return something like (using the values from above):
Gibson L-5 CES (1922) : $16,035.40

get_age() - which returns how old the guitar is in years (e.g., in 2022 the L-5 is: 2022 - 1922 = 100)

is_vintage() - which returns True if the guitar is 50 or more years old, False otherwise
Hint: try using get_age() to simplify the implementation of this method!
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years."""
        current_year = 2025  # Change this dynamically if needed
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, otherwise False."""
        return self.get_age() >= 50