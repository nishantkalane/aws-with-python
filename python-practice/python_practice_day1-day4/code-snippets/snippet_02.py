"""Snippet 2: Check whether a string is a palindrome, ignoring case.

Pattern: two pointers
Complexity: O(n) time

Interview answers
1. Logical correctness: Yes | I compare characters from both ends and move the
   pointers toward the center. If any pair differs, it is not a palindrome.
2. Edge cases:
   "madam" -> True, "hello" -> False, "a" -> True, "" -> True, "Madam" -> True
3. Production ready: No | The core logic is correct, but the implementation
   should clarify whether spaces and punctuation are ignored, and validate
   input if needed.
"""


def is_palindrome(s):
    s = s.lower()

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True


print(is_palindrome("Madam"))  # True
