"""
Word Count Program

This program processes multiple text files, generates word frequencies,
and outputs results to both the console and a file.

Usage:
    python3 word_count.py P3

Note:
Ensure that the files specified as command-line arguments exist and are readable.

The application utilizes the 'process_file', 'count_words', 'print_table', and 'write_to_file'
functions for file processing and output generation.

Author: Alejandra Mendoza Flores
Date: February 2, 2024
"""

import sys
import time

def process_file(file_name):
    """
    Reads the contents of a text file and returns a list of words.

    Parameters:
    - file_name (str): The name of the file to be processed.

    Returns:
    - list: A list containing the words extracted from the file.

    Raises:
    - FileNotFoundError: If the specified file is not found, an error message is printed,
      and an empty list is returned.

    Note:
    Ensure that the file exists and is readable. In case of a FileNotFoundError,
    an informative error message will be displayed, and an empty list will be returned.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            words = file.read().split()
            return words
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []

def count_words(words):
    """
    Counts the occurrences of each unique word in a list 
    and returns a dictionary with word frequencies.

    Parameters:
    - words (list): A list of words to be processed.

    Returns:
    - dict: A dictionary where keys are unique words and values are their respective frequencies.

    Note:
    - The input 'words' should be a list of strings representing words.
    - The function is case-sensitive, treating 'Word' and 'word' as different words.
    - Punctuation marks and special characters are considered part of the words.
    - If the input list is empty, an empty dictionary will be returned.
    """
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def print_table(file_name, word_count):
    """
    Prints a tabular representation of word frequencies in a file.

    Parameters:
    - file_name (str): The name of the file being analyzed.
    - word_count (dict): A dictionary containing word frequencies.

    Returns:
    - None: This function does not return any value but prints the table to the console.

    Note:
    - 'file_name' should be a string representing the name of the file being processed.
    - 'word_count' should be a dictionary with word frequencies.
    - The table displays the word and its corresponding frequency in a formatted manner.
    """
    print(f"\nFile: {file_name[:-4]}")
    print(f"{'Word':<15} {'Frequency':<10}")
    print("-" * 25)
    for word, count in word_count.items():
        print(f"{word:<15} {count:<10}")


def write_to_file(file_name, word_count):
    """
    Appends word frequency results to a text file in a tabular format.

    Parameters:
    - file_name (str): The name of the file being analyzed.
    - word_count (dict): A dictionary containing word frequencies.

    Returns:
    - None: This function does not return any value but appends the results to a file.

    Note:
    - 'file_name' should be a string representing the name of the file being processed.
    - 'word_count' should be a dictionary with word frequencies.
    - The results are appended to the 'WordCountResults.txt' file in a formatted tabular structure.
    """
    with open('WordCountResults.txt', 'a', encoding='utf-8') as result_file:
        result_file.write(f"\nFile: {file_name[:-4]}\n")
        result_file.write(f"{'Word':<15} {'Frequency':<10}\n")
        result_file.write("-" * 25 + "\n")
        for word, count in word_count.items():
            result_file.write(f"{word:<15} {count:<10}\n")
        result_file.write("\n")

def main():
    """
    Word counting application that processes multiple text files, generates word frequencies,
    and outputs results to both the console and a file.

    Usage:
    python wordCount.py <file1.txt> <file2.txt> ...

    Parameters:
    - None

    Returns:
    - None: This function does not return any value but prints results to the console
      and appends them to 'WordCountResults.txt'.t

    The function processes each specified file, prints word frequencies in a tabular format
    to the console, appends the results to 'WordCountResults.txt', and displays the total word count
    and execution time.

    Note:
    - Ensure that the files specified as command-line arguments exist and are readable.
    - The application utilizes the 'process_file', 'count_words', 'print_table', and 'write_to_file'
      functions for file processing and output generation.
    """
    start_time = time.time()

    if len(sys.argv) < 2:
        print("Usage: python wordCount.py <file1.txt> <file2.txt> ...")
        sys.exit(1)

    total_words_all_files = 0

    for file_name in sys.argv[1:]:
        words = process_file(file_name)
        total_words_all_files += len(words)
        word_count = count_words(words)
        print_table(file_name, word_count)
        write_to_file(file_name, word_count)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTotal words for all files: {total_words_all_files}")
    print(f"Total execution time: {elapsed_time:.4f} seconds\n")
    with open('WordCountResults.txt', 'a', encoding='utf-8') as result_file:
        result_file.write(f"\nTotal words for all files: {total_words_all_files}\n")
        result_file.write(f"Total execution time: {elapsed_time:.4f} seconds\n")

if __name__ == "__main__":
    main()
