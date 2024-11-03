"""
CP1404/CP5632 Practical
Language testing - Est. 10 minutes, Actual: 10 minutes

It should return a string like:
Python, Dynamic Typing, Reflection=True, First appeared in 1991
"""

from programming_language import ProgrammingLanguage

def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [python, ruby, visual_basic] # Create list of languages

    print("The dynamically typed languages are:") # Find and print languages with dynamic typing
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()