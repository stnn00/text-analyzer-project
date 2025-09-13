"""
text_analyzer.py

Reads a text file and prints:
- Total amount of words
- Number of unique words
- Frequency of each word
- Number of long words
"""

from collections import Counter # to replace manual word counting

def read_file(file_name):
    """Reads the text file assigned and returns it as a string."""
    with open(file_name, "r") as file:
        return file.read()

def lowercase_words(text):
    """Converts string to lowercase, removes punctuation, and splits it into a list."""
    for char in ".,/!?\:;'}{()[]<>|~@#$%^&*-_+=":
        text = text.replace(char, "")
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
            
    print(f"The total number of words is: {len(words)}")
    print(f"The unique words count is: {len(word_count)}")
    print(f"The most frequent words are:")
    for word, count in top_words:
        print(f"'{word}': {count}")
    print(f"Long words (more than 3 characters): {len(long_words_list)}")

if __name__ == "__main__":
    analyze_text("sample.txt")