"""
CP1404/CP5632 Practical
Guitar Collection Program
Estimate: 10 minutes
Actual:

Start the program and print a greeting.
Ask the user for guitar details (name, year, cost) in a loop until they enter a blank name.
Store each guitar as an object in a list.
After input is complete, print a list of all stored guitars.
Check if each guitar is vintage (50 years or older) and display it accordingly.
End the program.
"""

from prac_06.guitar import Guitar

def main():
    """Main function to run the guitar collection program."""
    guitars = []
    print("My guitars!")

def get_guitar():
    """Get user input for guitars and store them in a list."""
    guitars = []
    while True:
        name = input("Name: ")
        if name == "":
            break # When user leaves name blank, stops the program and gather final results
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
    return guitars

def display_guitars(guitars):
    """Display all guitars in the list with formatted output."""
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()