"""
A01081266 Ejercicio programacion
The program shall identify all
distinct words and the frequency of them
(how many times the word “X” appears in
the file).
"""
import sys
import time

def read_file(file_name):
    """Reads the file and returns a list of words."""
    words = []
    line_number = 0
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                line_number += 1

                # Remove leading and trailing whitespace from the line
                while line and line[0] in ' \t\n\r\f':
                    line = line[1:]
                while line and line[-1] in ' \t\n\r\f':
                    line = line[:-1]

                # Initialize an empty word
                word = ""

                # Iterate through each character in the line
                for char in line:
                    # If the character is whitespace
                    if char in ' \t\n\r\f':
                        # If there is a current word, append it to the list of words
                        if word:
                            words.append(word)
                            # Reset the word
                            word = ""
                    else:
                        # Add the character to the current word
                        word += char

                # If there is a pending word at the end of the line, append it to the list of words
                if word:
                    words.append(word)

    except FileNotFoundError:
        print("File not found.")
    except UnicodeDecodeError:
        print(f"Decoding error at line {line_number} of the file.")
    return words

def count_words(words):
    """Counts the frequency of each word in the list."""
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def main():
    """open the file and call the word count"""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithWords.txt")
        sys.exit(1)

    file_name = sys.argv[1]
    words = read_file(file_name)

    start_time = time.time()

    if words:
        word_count = count_words(words)

        end_time = time.time()
        elapsed_time_seconds = end_time - start_time
        elapsed_time_microseconds = elapsed_time_seconds * 1_000_000

        # Print results on screen
        print("Word count:")
        for word, count in word_count.items():
            print(f"{word}: {count}")

        print(f"Elapsed time: {elapsed_time_microseconds} microseconds")

        # Write results to file
        with open("WordCountResults.txt", 'w', encoding='utf-8') as result_file:
            result_file.write("Word count:\n")
            for word, count in word_count.items():
                result_file.write(f"{word}: {count}\n")
            result_file.write(f"Elapsed time: {elapsed_time_microseconds} microseconds\n")
    else:
        print("No valid data found in the file.")

if __name__ == "__main__":
    main()
