# unpythonic_analyzer.py

def analyze_text(file_name):
    # This function is full of bad practices.
    file = open(file_name, 'r')
    text = file.read()
    
    words = text.lower().split()
    
    # Let's count the occurrences of each word.
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    
    # Now let's find the words with more than 3 characters.
    long_words = []
    for word in words:
        if len(word) > 3:
            long_words.append(word)
            
    print("The total number of words is: " + str(len(words)))
    print("The unique words count is: " + str(len(word_count)))
    print("The most frequent words are:")
    
    for word, count in sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"'{word}': {count}")
    
    print("Long words (more than 3 characters): " + str(len(long_words)))
    
    file.close()

# You will need to create a text file named 'sample.txt' for testing.
analyze_text("sample.txt")