"""
CP1404/CP5632 Practical
Class for guitars - Est. 10 min

Remember the string formatting example from prac 2:

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
print(f"My guitar: {name}, first made in {year}")
You should notice that we have multiple values to store for one guitar entity: name, year and cost... and that guitars are awesome! What if we owned 9 guitars? We'd want to use a collection like a list... but what would each element in the list be? ... A tuple? A dictionary? No... This is a classic case for a class!

Write a Guitar class that allows you to store one guitar with these fields (attributes):

name
year
cost
Define the following methods:

__init__ - with defaults name="", year=0, cost=0

__str__ - which uses {} string formatting to return something like (using the values from above):
Gibson L-5 CES (1922) : $16,035.40

get_age() - which returns how old the guitar is in years (e.g., in 2022 the L-5 is: 2022 - 1922 = 100)

is_vintage() - which returns True if the guitar is 50 or more years old, False otherwise
Hint: try using get_age() to simplify the implementation of this method!

Remember that methods should not take in any data that the object already knows (like age, year, etc.).
"""
