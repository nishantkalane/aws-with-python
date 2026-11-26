"""Snippet 22: Find the first non-repeating character in a string.

Pattern: hashing / frequency counting
Complexity: O(n) time, O(k) extra space (k = distinct characters)

Two passes:
  1. count the frequency of every character
  2. traverse again and return the first character whose frequency is 1

Interview answers
1. Logical correctness: Yes | I count every character with a dictionary, then
   traverse the original string and return the first character whose count is
   exactly one.
2. Edge cases:
   "swiss" -> "w", "aabb" -> None, "abcdef" -> "a", "aabbc" -> "c", "" -> None
3. Production ready: Yes, for a basic utility | O(n) time and O(k) extra space.
   I'd clarify whether comparison is case-sensitive and whether spaces count.
"""


def first_non_repeating(s):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    for char in s:
        if freq[char] == 1:
            return char

    return None


print(first_non_repeating("swiss"))  # w
print(first_non_repeating("aabb"))   # None
