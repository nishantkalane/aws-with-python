"""Snippet 47: Read a text file and count its lines, words and characters.

Pattern: file handling / string processing
Complexity: O(n) time, O(n) space (the whole file is read into memory)

Run from this folder: it reads sample.txt next to the file.
splitlines() counts logical lines; split() counts whitespace-separated words;
len(content) counts characters (Unicode code points), not bytes.

Interview answers
1. Logical correctness: Yes | I open the file with a context manager, read
   its contents, and use string operations to count lines, words and
   characters. The context manager closes the file automatically.
2. Edge cases:
   - File with multiple lines
   - File with one line
   - Empty file -> (0, 0, 0)
   - File containing only spaces
   - File containing punctuation
   - File containing Unicode characters
3. Production ready: No | Reading the whole file into memory can be expensive
   for large files. I'd process it line by line and handle FileNotFoundError
   and PermissionError.
"""


def count_file_contents(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    lines = len(content.splitlines())
    words = len(content.split())
    characters = len(content)

    return lines, words, characters


print(count_file_contents("sample.txt"))
# (3, 13, 76) for the sample.txt in this folder
