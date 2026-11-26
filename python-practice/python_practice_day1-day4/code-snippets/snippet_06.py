"""Snippet 6: Remove duplicates from a list while preserving order.

Pattern: traversal / membership checking
Complexity: O(n^2) time (membership check on a list is O(n))

Interview answers
1. Logical correctness: Yes | I traverse the list and add an element only if
   it is not already in the result list, so duplicates are removed and the
   original order is preserved.
2. Edge cases:
   [1,1,2,3,2] -> [1,2,3], [5,5,5] -> [5], [1,2,3] -> [1,2,3], [] -> []
3. Production ready: No | The logic is correct, but membership checking in a
   list makes it O(n^2). For large inputs I'd use a set for fast lookup, with
   a separate result list to keep the order.
"""


def remove_duplicates(lst):
    unique = []

    for item in lst:
        if item not in unique:
            unique.append(item)

    return unique


print(remove_duplicates([1, 1, 2, 4, 1, 3, 2]))
# [1, 2, 4, 3]
