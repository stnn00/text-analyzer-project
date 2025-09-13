"""
text_analyzer.py

Reads a text file, prints total amount of words, frequency of each word, total of unique words, and long words.
"""

from collections import Counter
""" Collections is a built-in module in Python that allows us to have different kinds of data types to store, sort through, and utilize"""

def analyze_text(file_name):
    """
    Reads the text file assigned and prints:
    - Total number of words
    - Amount of unique words
    - Top 5 most frequent words
    - Words longer than 3 characters

    """
    
    with open(file_name, "r") as file:
        text = file.read()
    
    words = text.lower().split()
    
    word_count = Counter(words)
    
    long_words = [word for word in words if len(word) > 3]
            
    print("The total number of words is: " + str(len(words)))
    print("The unique words count is: " + str(len(word_count)))
    print("The most frequent words are:")
    
    for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"'{word}': {count}")
    
    print("Long words (more than 3 characters): " + str(len(long_words)))

analyze_text("sample.txt")