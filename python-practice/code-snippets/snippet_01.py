"""Snippet 1: Reverse a string without slicing or reversed().

Pattern: reverse traversal
Complexity: O(n) time

Interview answers
1. Logical correctness: Yes | I traverse the string backward and append each
   character to a new string, which reverses it without slicing or reversed().
2. Edge cases:
   "hello" -> "olleh", "a" -> "a", "" -> "", "12345" -> "54321"
3. Production ready: No | The logic is correct, but repeated string
   concatenation can be inefficient for large strings. For production I'd use
   a more efficient approach and add input validation if required.
"""


def reverse_string(s):
    rev = ""

    for i in range(len(s) - 1, -1, -1):
        rev += s[i]

    return rev


print(reverse_string("nish"))  # hsin
