"""Sentiment analysis script for hotel reviews.

This script analyzes hotel review text to count positive and negative
sentiment words using the text analysis module.
"""

from textanalysis.textanalysis import count_words

nb_positive_words = count_words('hotel-reviews.txt', ['good', 'great'])
"""int : Number of positive sentiment words found in the hotel reviews."""

nb_negative_words = count_words('hotel-reviews.txt', ['bad', 'awful'])
"""int : Number of negative sentiment words found in the hotel reviews."""

print("{} positive words.".format(nb_positive_words))
print("{} negative words.".format(nb_negative_words))
