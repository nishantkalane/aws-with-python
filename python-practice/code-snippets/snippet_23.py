"""Snippet 23: Find the longest word in a sentence.

Pattern: traversal / maximum tracking
Complexity: O(n) time, n = total sentence length

Interview answers
1. Logical correctness: Yes | I start with the first word as the longest and
   compare the length of every other word, updating when I find a longer one.
2. Edge cases:
   "Python is interesting" -> "interesting", "I love coding" -> "coding",
   "cat dog ant" -> "cat" (first of the ties), "hello" -> "hello", "" -> None
3. Production ready: Yes, for a basic utility | O(n). For production I'd clarify
   how punctuation, multiple spaces and ties should be handled.
"""


def longest_word(sentence):
    words = sentence.split()

    if len(words) == 0:
        return None

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


print(longest_word("Python programming is interesting"))
# programming
