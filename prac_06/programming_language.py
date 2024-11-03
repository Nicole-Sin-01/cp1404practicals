"""
CP1404/CP5632 Practical
Class for programming languages - Est. 15 min, Actual: 10 minutes

Define the following methods:
__init__ - like most init functions, create the fields and set them to the parameters passed in.

is_dynamic() - which returns True/False if the programming language is dynamically typed or not.

[IMPORTANT] Please understand that this function will take no parameters other than self. The data is already inside the object, so you don't need to tell the object its own data.

This function's purpose is to encapsulate the functionality that would make the class more helpful.
See how the function name starts with is, like isupper(), isnumeric(), etc.?
So, it returns a Boolean.
"""

class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance.
        name: string, reference name for programming language
        typing: string, typing discipline of the language, Static or Dynamic
        reflection: string, whether the language supports reflection, Yes or No
        year: integer, release year of the language
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamic, else False."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a formatted string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
