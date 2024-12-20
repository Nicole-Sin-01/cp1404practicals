"""
CP1404/CP5632 Practical
List exercises

Write a program that prompts the user for 5 numbers and then stores each of these in a list called numbers.
The program should then output information about these numbers, as in the output below.
You can use the functions min, max, sum and len, and you can use the append method to add a number to a list.

   Number: 5
   Number: 20
   Number: 1
   Number: 2
   Number: 3
   The first number is 5
   The last number is 3
   The smallest number is 1
   The largest number is 20
   The average of the numbers is 6.2
"""
# 1. Basic list operations
def main():
    """Main function to run code"""
    numbers = get_numbers()  # Get the list of numbers from the user
    print_results(numbers)

def get_numbers():
    """Prompt the user for 5 numbers and validate each one."""
    numbers = []  # List to store valid numbers
    for i in range(5):
        valid_input = False  # Flag to track if the input is valid
        while not valid_input:
            try:
                number = int(input(f"Enter number: "))
                numbers.append(number)  # Add the valid number to the list
                valid_input = True
            except ValueError:
                print("Invalid input; please enter a valid number.")
    return numbers

def print_results(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

main()

#2. Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")