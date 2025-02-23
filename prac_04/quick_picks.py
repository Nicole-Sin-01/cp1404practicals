import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

def main():
    quick_picks_count = get_valid_pick("Enter number of picks:  ")

def get_valid_pick(prompt):
    """Keeps validating and returns value only when a valid integer is entered"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a number more than 0.")
        except ValueError:
            print("Invalid input. Try again.")

main()
