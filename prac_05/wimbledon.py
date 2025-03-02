"""
CP1404/CP5632 Practical
Wimbledon File Processing
Estimate: 10 minutes
Actual:  minutes

Remember to include your estimate and actual time in the module docstring.

Save the wimbledon.csv data file provided.
This is based on the Wikipedia entry Wimbledon gentlemen's singles champions .

Write a program to read this file, process the data and display processed information:

the champions and how many times they have won.
the countries of the champions in alphabetical order
Requirements and Hints
You need to store the data in appropriate data structures.
The solution uses: a list of lists, a dictionary and a set.

The file is not in simple ASCII format but UTF-8 with a byte order mark, or BOM.
You can account for this by setting the encoding like:

with open(filename, "r", encoding="utf-8-sig") as in_file:
For the final output of countries, use the join method to create a single string.

Use functions for each logical step/chunk of the program.
If you write it all in main to start with, that's fine, but then refactor it.
The solution uses 4 functions including main.

Sample output (truncated)
Wimbledon Champions:
Rod Laver 2
...
Lleyton Hewitt 1
Roger Federer 8
Rafael Nadal 2
Novak Djokovic 7
Andy Murray 2

These 12 countries have won Wimbledon:
AUS, CRO, ESP, FRG, GBR, GER, NED, SRB, SUI, SWE, TCH, USA

"""

def read_wimbledon_data(filename):
    """Read CSV file and return data as a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()[1:]
        return [line.strip().split(',') for line in lines]

def count_champions(data):
    """Count how many times each player has won Wimbledon."""
    champion_to_wins = {}
    for row in data:
        champion = row[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins
