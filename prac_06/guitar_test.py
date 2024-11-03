"""
CP1404/CP5632 Practical
Guitar testing - Est. 10 minutes, Actual: 5 minutes

Now write a program with at least enough code to test that the last two methods work as expected.
To test get_age(), you could test that the above example guitar does indeed output 100 as expected. Here's some sample output for testing two guitars where the second is called Another Guitar and has year=2013:

Gibson L-5 CES get_age() - Expected 100. Got 100
Another Guitar get_age() - Expected 9. Got 9
Gibson L-5 CES is_vintage() - Expected True. Got True
Another Guitar is_vintage() - Expected False. Got False
Do you see how this works?

We print our own literal for what we expect if the function works (e.g., 100), then we print what the method actually returns, and we look at the output to see if they match.
This form of testing is quite 'manual' since we need to read the output and compare it ourselves, but it is a good start.

Let's say we wrote the is_vintage() method incorrectly, then we want to see something like:

50-year old guitar is_vintage() - Expected True. Got False
We can see that the actual does not match the expected, so we know we need to fix something
"""

from guitar import Guitar

def main():
    # Create two guitar instances
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1000)

    # Test get_age()
    print(f"{guitar1.name} get_age() - Expected 102. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 11. Got {guitar2.get_age()}")

    # Test is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

if __name__ == "__main__":
    main()