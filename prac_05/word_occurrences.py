"""
CP1404/CP5632 Practical

Write a program to count the occurrences of words in a string.
The program should ask the user for a string, then print the counts of how many of each word are in the string.
The output should look like this (depending on user input):

Text: this is a collection of words of nice words this is a fun thing it is
a : 2
collection : 1
fun : 1
is : 3
it : 1
nice : 1
of : 2
thing : 1
this : 2
words : 2

Use a dictionary where the keys are the words and the values are the counts;
When you find a word, check if it's in the dictionary...

Notice that the sample output is sorted.
Only after you have the program working, make your program do this sorting.

Now align the outputs so the numbers are in one nice column. You will need to find the longest word in the list first.
Then you can use f-string formatting and a variable width.
This can be done with another {} placeholder, like in this example:

thing, width, other_thing = "first", 13, "second"
print(f"{thing:{width}} = {other_thing}")

This formats the first placeholder value, thing, with a width of width then prints a literal = then the value of other_thing.
Your output should then look something like:

  a          : 2
  collection : 1
  fun        : 1
"""

def main():
    user_text = input("Text: ").strip()
    words = user_text.split()
    word_counts = get_word_count(words)

    max_word_length = max(len(word) for word in word_counts) # Find the longest word for formatting

    for word in sorted(word_counts):
        print(f"{word:{max_word_length}} : {word_counts[word]}") # Print the words, alphabetically sorted and aligned

def get_word_count(words):
    """Counts occurrences of words in a list and returns a dictionary."""
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1
    return word_to_count

main()
