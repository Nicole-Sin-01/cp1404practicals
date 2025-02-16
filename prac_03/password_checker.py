"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
Write a program that asks for and validates a person's password. The program is not for comparing a password to a known password, but validating the 'strength' of a new password, like you see on websites: enter your password, and then it tells you if it's valid (matches the required pattern) and re-prompts if it's not.
All passwords must contain at least one each of:
digit
lowercase letter
uppercase letter

The starter code uses constants to store:
the minimum and maximum length of the password
whether a special character is required (note the Boolean naming)
the special characters (as a string; a list is not necessary)

Remember when a program has CONSTANTS, you should use them everywhere you can so that if you change them at the top, this change affects the whole program as expected.
E.g., if you changed the minimum length to 5, the program should print 5 and should check to make sure the password is >= 5 characters long.

"""

MIN_LENGTH = 5
MAX_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")