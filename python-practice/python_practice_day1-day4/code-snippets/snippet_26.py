"""Snippet 26: Find common elements between two lists.

Pattern: hashing / membership checking
Complexity: O(n + m) average time, O(n) extra space

Interview answers
1. Logical correctness: Yes | I store the first list's elements in a set,
   then traverse the second list and check for membership. I use another set
   to avoid adding duplicate common elements.
2. Edge cases:
   - [1, 2, 3], [2, 3, 4] -> [2, 3]
   - [1, 1, 2], [1, 1, 3] -> [1]
   - [1, 2], [3, 4] -> []
   - [], [1, 2] -> []
   - [5], [5] -> [5]
3. Production ready: Yes, for a basic utility | Average time is O(n + m)
   using O(n) extra space. I'd clarify whether duplicates should appear once
   or keep their frequency in the result.
"""


def common_elements(a, b):
    seen = set()
    common = []

    for num in a:
        seen.add(num)

    added = set()

    for num in b:
        if num in seen and num not in added:
            common.append(num)
            added.add(num)

    return common


print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
# [3, 4]
