"""
text_analyzer.py

Reads a text file, prints total amount of words, frequency of each word, total of unique words, and long words.
"""

from collections import Counter
""" Collections is a built-in module in Python that allows us to have different kinds of data types to store, sort through, and utilize"""

def read_file(file_name):
    """Reads the text file assigned and returns it as a string."""
    with open(file_name, "r") as file:
        return file.read()

def lowercase_words(text):
    """Converts string to lowercase and splits it into a list."""
    return text.lower().split()

def count_word(words_list):
    """Counts the frequency of each word in words_list using Counter object."""
    return Counter(words_list)

def frequent_words(word_count, n=5):
    """Returns the top n most frequent words as a list of tuples (word, count).

    n variable means number of items, can be replaced.
    """
    return word_count.most_common(n)

def count_long_words(words_list, min_length=3):
    """Counts and returns a list of words longer than min_length.

    min_length: minimum length of words, default is 3.
    """
    return [word for word in words_list if len(word) > min_length]

def analyze_text(file_name):
    """
    Reads a text file and prints:
    - Total amount of words
    - Total of unique words
    - Top frequent words
    - Total of long words
    """
    text = read_file(file_name)
    words = lowercase_words(text)
    word_count = count_word(words)

    top_words = frequent_words(word_count)
    long_words_list = count_long_words(words)
            
    print("The total number of words is: {len(words)}")
    print("The unique words count is: " + str(len(word_count)))
    print("The most frequent words are:")
    
    for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"'{word}': {count}")
    
    print("Long words (more than 3 characters): " + str(len(long_words_list)))

analyze_text("sample.txt")