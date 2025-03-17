"""
CP1404/CP5632 Practical
Programming Language Program
Estimate: 5 minutes
Actual: 5 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    """Test ProgrammingLanguage class and display dynamically typed languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # print(python) # Test the string representation
    get_dynamic([python, ruby, visual_basic])

def get_dynamic(languages):
    """Print the dynamically typed languages from the given list."""
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()