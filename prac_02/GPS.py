"""
CP1404 - Practical 2
GPS (Gopher Population Simulator)

A secret population of 1000 gophers lives near the library.
Every year, a random number of gophers is born, between 10% of the current population, and 20%.
(e.g. 15% of the gophers might give birth, increasing the population by 150).
Also, each year a random number of gophers die, between 5% and 25% (e.g. 8% of the gophers might die, reducing the population by 80).

Write a program that simulates a population of gophers over a ten-year period and displays each year's population size.
The output should look something like this (it's random, so yours won't be the same):

   Welcome to the Gopher Population Simulator!
   Starting population: 1000
   Year 1

   145 gophers were born. 228 died.
   Population: 917
   Year 2

   124 gophers were born. 152 died.
   Population: 889
   Year 3

   138 gophers were born. 180 died.
   Population: 847
"""

import random

STARTING_POPULATION = 1000
TIME_PERIOD = 10
MINIMUM_BIRTH_RATE = 0.1
MAXIMUM_BIRTH_RATE = 0.2
MINIMUM_DEATH_RATE = 0.05
MAXIMUM_DEATH_RATE = 0.25

def main():
    """Main function to drive the GPS program."""
    current_population = STARTING_POPULATION
    print(f"Welcome to the Gopher Population Simulator!\nStarting population: {STARTING_POPULATION}")

    # Simulate the births and deaths of the gophers
    for year in range(1, TIME_PERIOD + 1):
        print(f"\nYear {year}")

        # Get births and deaths based on current population
        born_gophers = get_birthed_gophers(current_population)
        dead_gophers = get_dead_gophers(current_population)

        # Update the population based on births and deaths
        current_population = update_population(current_population, born_gophers, dead_gophers)

        # Display the results
        print(f"{born_gophers} were born. {dead_gophers} died.")
        print(f"Population: {current_population}")

def get_birthed_gophers(current_population):
    """Calculate the number of gophers born."""
    birth_rate = random.uniform(MINIMUM_BIRTH_RATE, MAXIMUM_BIRTH_RATE)
    return int(current_population * birth_rate)

def get_dead_gophers(current_population):
    """Calculate the number of gophers that died."""
    death_rate = random.uniform(MINIMUM_DEATH_RATE, MAXIMUM_DEATH_RATE)
    return int(current_population * death_rate)

def update_population(current_population, born_gophers, dead_gophers):
    """Update the current population based on births and deaths."""
    return current_population + born_gophers - dead_gophers

main()
