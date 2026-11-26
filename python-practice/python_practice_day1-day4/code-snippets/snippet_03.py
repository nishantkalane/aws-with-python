"""Snippet 3: Count vowels in a string.

Pattern: traversal / counting
Complexity: O(n) time

Interview answers
1. Logical correctness: Yes | I traverse each character and increment the
   counter whenever it is a vowel. The final counter is the vowel count.
2. Edge cases:
   "hello" -> 2, "AEIOU" -> 5, "rhythm" -> 0, "" -> 0, "Education" -> 5
3. Production ready: Yes, for a basic utility | Simple, readable and efficient
   for ordinary inputs. For a larger application I'd define how Unicode
   vowels and invalid inputs are handled.
"""


def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count


print(count_vowels("Nishant"))  # 2
