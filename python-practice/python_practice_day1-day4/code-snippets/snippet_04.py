"""Snippet 4: Find the frequency of each character in a string.

Pattern: hashing / frequency counting
Complexity: O(n) time

Interview answers
1. Logical correctness: Yes | I use a dictionary to store each character and
   its count. If the character exists I increment it, otherwise I set it to 1.
2. Edge cases:
   "hello" -> l: 2, "aaaa" -> a: 4, "abc" -> every count is 1, "" -> {}
3. Production ready: Yes, for a basic utility | Correct and efficient. For
   production I'd clarify whether counting is case-sensitive and whether
   spaces are included.
"""


def character_frequency(s):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


print(character_frequency("hello"))
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
