"""
CP1404/CP5632 Practical
Hexadecimal Colour Code Lookup
Allows the user to look up hexadecimal codes for common color names.

Estimated: 5 minutes
Actual: 15 minutes
"""

# Dictionary of color names and their corresponding hex codes
COLOR_TO_HEX = {"Amethyst": "#9966cc", "DarkOrchid": "#9932cc", "Heliotrope": "#df73ff", "Lavender": "#e6e6fa",
                "Lilac": "#c8a2c8", "Mauve": "#e0b0ff", "Orchid": "#da70d6", "Periwinkle": "#ccccff", "Plum": "#dda0dd",
                "Thistle": "#d8bfd8"}

print("Hexadecimal Colour Code Lookup")
print("Available colours:", ", ".join(COLOR_TO_HEX.keys())) # Lists the names of available colours in the dictionary

color_name = input("Please enter a color name to get its hex code: ").strip().lower()
while color_name:
    if color_name in COLOR_TO_HEX:
        print(f"The hex code for {color_name} is {COLOR_TO_HEX[color_name]}")
    else:
        print("Invalid color name. Please try again.")
    color_name = input("Enter color name: ").strip().lower()

print("Goodbye!")