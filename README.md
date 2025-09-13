# text-analyzer-project README
A Python script to calculate total amount of words in a .txt file, prints number of unique words, the frequency of each word, and the total of long words.

## About text_analyzer.py
text_analyzer.py reads a text file and prints:<br>
- Total number of words<br>
- Number of unique words<br>
- Top 5 most frequent words<br>
- Number of long words (more than 3 characters)<br>

The script lowercases all words and removes punctuation to accurately count words in a .txt file<br>

## Instructions
<br>
1. Set a text file to analyze (e.g., sample.txt). Place it in the same folder directory path as text_analyzer.py<br>
2. Run the script<br>
3. The script will automatically analyze the provided .txt file. To analyze another file, modify the line `your_file_name.txt` at the bottom of the script with the name of the .txt file:<br>
```python
if __name__ == "__main__":
    analyze_text("your_file_name.txt")