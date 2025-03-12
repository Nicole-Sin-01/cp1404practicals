"""
CP1404/CP5632 Practical
Programming Language Program
Estimate: 5 minutes
Actual:
"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    """Test ProgrammingLanguage class and display dynamically typed languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

main()