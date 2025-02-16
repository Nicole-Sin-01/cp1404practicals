"""
CP1404/CP5632 - Practical
Refactored program to determine score status
"""

import random

# Constants
MINIMUM_THRESHOLD = 0
MAXIMUM_THRESHOLD = 100
PASSABLE_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90

def main():
    # Get a valid score from the user
    score = get_valid_score()

    # Print the result for the user's score
    result = determine_result(score)
    print(f"Score Result: {result}")

    # Generate a random score and print its result
    random_score = random.uniform(MINIMUM_THRESHOLD, MAXIMUM_THRESHOLD)
    print(f"\nRandom score: {random_score:.0f}")
    random_result = determine_result(random_score)
    print(f"Random score result: {random_result}")

if __name__ == "__main__":
    main()
