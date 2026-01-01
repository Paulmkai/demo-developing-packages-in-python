"""Text analysis script for counting word occurrences.

This module reads a text file and counts how many times specific words
appear in the text using case-insensitive matching.

Notes
-----
Reads 'alice.txt' and counts occurrences of 'cat' and 'cats'.
"""

# Open the text file
with open('alice.txt') as file:
    # Read the contents of the file
    text = file.read()

n = 0

for word in text.split():
    # Count the number of times the words in the list appear
    if word.lower() in ['cat', 'cats']:
       n += 1

print("Lewis caroll uses the word 'cat' {} times".format(n))
