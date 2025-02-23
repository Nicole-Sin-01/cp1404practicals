import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

def main():
    quick_picks_count = get_valid_pick("Enter number of picks:  ")

    for i in range(quick_picks_count):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))

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

def generate_quick_pick():
    """Generate a single row of random numbers"""
    quick_pick = []

    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick

main()
