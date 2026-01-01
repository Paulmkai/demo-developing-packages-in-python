"""Romantic word analysis script for love poems.

This script analyzes romantic poetry text to count occurrences of
romantic sentiment words using the text analysis module.
"""

from textanalysis.textanalysis import count_words

romantic_word = count_words('romantic_love_poem.txt', ['love'])
"""int : Number of romantic words (love) found in the poem."""
                            
print('{} romantic words'.format(romantic_word))