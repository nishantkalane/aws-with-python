"""Snippet 5: Check whether two strings are anagrams.

Pattern: frequency counting / hashing
Complexity: O(n) time

Interview answers
1. Logical correctness: Yes | I check the lengths first, count the characters
   of the first string, then decrease the counts using the second string. If a
   character is missing or a count goes negative, they are not anagrams.
2. Edge cases:
   "listen","silent" -> True, "hello","world" -> False, "aab","aba" -> True,
   "aab","abb" -> False, "","" -> True, different lengths -> False
3. Production ready: Yes, for a basic utility | Efficient at O(n). For
   production I'd define whether case, spaces and punctuation are ignored
   before comparing.
"""


def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    for char in s1:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    for char in s2:
        if char not in freq:
            return False

        freq[char] -= 1

        if freq[char] < 0:
            return False

    return True


print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
