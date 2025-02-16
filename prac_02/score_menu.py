"""
CP1404 - Practical 2
Score Menu Program

def main()
    menu
        Option 1: Get valid score
        Option 2: Print result
        Option 3: Show stars
        Option 4: Quit
        Invalid Option

def get_valid_score()
    input score
    while score < minimum or > maximum
        print invalid message
        input score

def determine_result
    if score >= 90
        return excellent
    if score >= 50
        return passable
    else
        return bad

def print_stars()
    print score * "*"
"""

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASSABLE_THRESHOLD = 50
EXCELLENT_THRESHOLD = 90


def main():
    """Main function to handle the score menu."""
    print("Welcome to the Score Menu Program!")

    score = get_valid_score()

    # Display the menu and get the user's choice
    choice = ""
    while choice != "Q":
        print_menu()
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
