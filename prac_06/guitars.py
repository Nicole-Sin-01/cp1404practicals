"""
CP1404/CP5632 Practical
Program that uses the guitar class - Est. 10 minutes

his program should use a list to store all the user's guitars (keep inputting until they enter a blank name), then print their details.

Important

Read the full question including the notes before starting.
We've written helpful guidance to make this easier and to teach you valuable lessons.

Sample Output (bold is user entry):

My guitars!
Name: Fender Stratocaster
Year: 2014
Cost: $765.4
Fender Stratocaster (2014) : $765.40 added.

Name:

... snip ...

These are my guitars:
Guitar 1:       Gibson L-5 CES (1922), worth $ 16,035.40 (vintage)
Guitar 2:        Line 6 JTV-59 (2010), worth $  1,512.90
Guitar 3:  Fender Stratocaster (2014), worth $    765.40
Programmer Efficiency Note
When testing a program like this you can waste a lot of time typing in input... then changing something, running it again and... typing the same thing again...
So don't do it!

Instead, comment out the user input lines, and put in lines like this to 'get' the data for testing:

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
According to Wikipedia's page on the abstraction principle:

"When read as recommendation to the programmer, the abstraction principle can be generalised as the "don't repeat yourself" principle, which recommends avoiding the duplication of information in general, and also avoiding the duplication of human effort involved in the software development process."

Notes (you haven't started yet, have you?)
The sample output uses some nice string formatting. Feel free to try and figure this out, or just use something like our code below (the width we use for guitar.name is just a guesstimate):

print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
The variable vintage_string is set to "" or " (vintage)" depending on the is_vintage() method.
If you're keen, try using Python's ternary operator to do this in one line.
E.g., to set the value of category to adult or child depending on age, you could use:

category = "adult" if age >= 18 else "child"
For this particular code, we've used both i and the target variable guitar (instead of guitars[i]) by using the built-in enumerate() function.

for i, guitar in enumerate(guitars, 1):
    # do something with i (the index) and guitar (the element)

"""


