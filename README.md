# text-analyzer-project README
A Python script to calculate total amount of words in a *.txt* file, prints number of unique words, the frequency of each word, and the total of long words.

## About text_analyzer.py
*text_analyzer.py* reads a text file and prints:<br>
- Total number of words<br>
- Number of unique words<br>
- Top 5 most frequent words<br>
- Number of long words (more than 3 characters)<br>

The script lowercases all words and removes punctuation to accurately count words in a *.txt* file<br>

## Demonstration
Video on YouTube to demonstrate and explain python script (3:30)
- https://youtu.be/mP4ChU7rsoU

## Instructions
1. Set a *.txt* file to analyze (e.g., sample.txt). Place it in the same folder/directory path as *text_analyzer.py*<br>
2. Run the script<br>
3. The script will automatically analyze the provided *.txt* file. To analyze another file, modify the line `your_file_name.txt` at the bottom of the script with the name of the *.txt* file:<br>
```python
if __name__ == "__main__":
    analyze_text("your_file_name.txt")
```

## Key Refactoring Improvements

- **PEP 8 compliance** - Adjusted naming conventions to follow PEP 8 guidelines.<br>
- **Context Manager** - Replaced manual file handling `open()` and `close()` calls with `with` statements to implement automatic file handling and ensure proper management.<br>
- **List Comprehensions** - Simplified the logic using `for` loops, to improve code readability.<br>
- **`collections./Counter`** - Replaced manual word-counting loops with `Counter` for efficient calculation and to improve readability.<br>

The refactoring improvements improved modularity, maintainable, and Pythonic, while retaining the script's intended functionality.
