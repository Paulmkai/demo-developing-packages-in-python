"""Text analysis module for counting word occurrences in files.

Provides utilities for analyzing text files and counting occurrences
of specified words with case-insensitive matching.
"""


def count_words(filepath, word_list):
    """Count occurrences of words in a text file.

    Parameters
    ----------
    filepath : str
        Path to the text file to analyze.
    word_list : list of str
        List of words to count. Matching is case-insensitive.

    Returns
    -------
    int
        Total count of occurrences of all words from word_list in the file.

    Examples
    --------
    >>> count = count_words('alice.txt', ['cat', 'cats'])
    >>> print(count)
    42
    """
    with open(filepath) as file:
        text = file.read()
    n = 0
    for word in text.split():
        if word.lower() in word_list:
            n += 1
    return n