"""
CP1404 - Practical
Convert Fahrenheit temperatures to Celsius and save the results.

def generate_temperatures()
    open file using write
    for i in range(number_of_temperatures):
        temperature = random.uniform(-200, 200)
        file write

def fahrenheit_to_celsius(fahrenheit):
   (fahrenheit - 32) * 5.0 / 9.0

def read_temperatures()
    open file using read
    line strip in float

def write_temperatures()
    open file using write

def main()
"""

import random

def main():
    """Main program to generate and convert temperatures."""
    input_file = "temps_input.txt"
    output_file = "temps_output.txt"

    generate_temperatures(input_file)
    fahrenheit_temps = read_temperatures(input_file) # Read fahrenheit temperatures in input file
    celsius_temps = [fahrenheit_to_celsius(temp) for temp in fahrenheit_temps] # Celsius conversion
    write_temperatures(celsius_temps, output_file) # Write Celsius temperatures to output file

if __name__ == "__main__":
    main()