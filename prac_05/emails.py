"""
CP1404/CP5632 Practical
Emails Program
Estimate: 5 minutes
Actual:  minutes

Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Remember to use our naming convention for dictionaries, key_to_value.

Ask the user for an email until they enter a blank one.
Use a separate function to extract a name from the email as in the example below.
You should find the following methods useful: split, join, title.

Notice the prompt to check if the name is correct: Y/n

In our program, if the user does not press Enter or Y, then ask for their name.
Once you have stored all the emails and names, just loop through the dictionary (use the items method) and print them out.
"""

def main():
    email_to_name = {}

    email = input("Email: ").strip()
    while email:
        email_to_name[email] = None  # Placeholder for now
        email = input("Email: ").strip()

main()
