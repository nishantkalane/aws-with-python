"""Program 7: Count lines, words and characters in a text file.

Reads sample.txt (in this folder) and prints the totals.

TC: O(C), C = total number of characters
SC: O(L), L = maximum line length being processed
Concept: file handling / string processing
Notes:
  - open() opens the file; "with" closes it automatically.
  - split() separates words on whitespace.
  - len(line) counts characters, including the newline when present.
"""


def count_file(filename):
    lines = 0
    words = 0
    characters = 0

    with open(filename, "r") as file:
        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line)

    print("Lines:", lines)
    print("Words:", words)
    print("Characters:", characters)


count_file("sample.txt")
