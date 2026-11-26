"""Program 1: Find the second non-repeating character in a string.

Example: s = "swiss" -> "i"
(Non-repeating characters in order are "w", then "i", so the second is "i".)

TC: O(n)
SC: O(k), k = number of distinct characters
Concept: Hashing / frequency counting
Note: keep the original string order when picking the second character.
"""


def second_non_repeating(s):
    freq = {}

    # Step 1: count the frequency of each character
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Step 2: find the second non-repeating character
    count = 0
    for ch in s:
        if freq[ch] == 1:
            count += 1
            if count == 2:
                return ch
    return None


s = "swiss"
print(second_non_repeating(s))
