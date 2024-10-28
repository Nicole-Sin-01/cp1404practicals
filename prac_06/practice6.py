# """
# Write a list comprehension to produce a new list containing only the monsters that have more than 16 teeth
# """
# TOOTHY_THRESHOLD = 16
#
# monsters = [["Mike", 340, "blue"], ["James", 14, "green"], ["Randall", 24, "purple"]]
#
# toothy_monsters = [monster for monster in monsters if monster[1] > TOOTHY_THRESHOLD]
#
# print(toothy_monsters)

"""
Write a Monster class definition
A Monster knows: name (str), number_of_teeth (int) and colour (str).
Use default vales "Mike" 0, "blue" for these 3 attributes respectively

Write a method called is_scary. A monster is scary if it has more than 16 teeth or is red
Include docstrings for your class and methods.
"""

class Monster:
    """Represent a Monster object."""

    def __init__(self, name="Mike", number_of_teeth=0, colour="blue"):
        """Initialise a Monster instance.

        name: string, reference name for monster
        number_of_teeth: integer, number of teeth of a monster
        colour: string, colour of monster
        """
        self.name = name
        self.number_of_teeth = number_of_teeth
        self.colour = colour

    def __str__(self):
        """Return a string representation of a Monster object."""
        return f"{self.name}, {self.number_of_teeth}, {self.colour}"

    def is_scary(self):
        """Determine if a monster is scary. A monster is considered scary if it has more than 16 teeth or is red."""
        return self.number_of_teeth > 16 or self.colour == "red"

# Create a list of Monster instances
monsters = [
    Monster("Mike", 15, "blue"),
    Monster("Sully", 20, "purple"),
    Monster("Randall", 10, "red"),
    Monster("Boo", 5, "green")
]

# List comprehension to filter for scary monsters
scary_monsters = [monster for monster in monsters if monster.is_scary()]

# Check if each monster is scary and print them if they are
for monster in scary_monsters:
        print(monster.name)