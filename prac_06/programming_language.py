"""
CP1404/CP5632 Practical
Programming Language Class
Estimate: 5 minutes
Actual:
"""

class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year