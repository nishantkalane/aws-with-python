"""Snippet 44: Group a list of words by their first letter.

Pattern: hashing / dictionary grouping
Complexity: O(n) time, O(n) space (n = number of words)

Interview answers
1. Logical correctness: Yes | I use the first letter of each word as a
   dictionary key. If the key exists I append the word, otherwise I create a
   new list for that letter.
2. Edge cases:
   - ["apple", "ant", "banana"] -> {'a': ['apple', 'ant'], 'b': ['banana']}
   - ["Cat", "car", "Dog"] -> {'c': ['Cat', 'car'], 'd': ['Dog']}
   - ["apple"] -> {'a': ['apple']}
   - [] -> {}
   - ["", "apple"] -> {'a': ['apple']}
3. Production ready: No | The grouping is efficient, but it silently skips
   empty strings. I'd explicitly define how empty words, non-string values
   and Unicode characters are handled.
"""


def group_by_first_letter(words):
    groups = {}

    for word in words:
        if len(word) == 0:
            continue

        first = word[0].lower()

        if first not in groups:
            groups[first] = []

        groups[first].append(word)

    return groups


words = ["apple", "ant", "banana", "ball", "cat"]

print(group_by_first_letter(words))
# {'a': ['apple', 'ant'], 'b': ['banana', 'ball'], 'c': ['cat']}
