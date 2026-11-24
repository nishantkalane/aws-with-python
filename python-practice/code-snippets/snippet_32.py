"""Snippet 32: Return all duplicate values in a list.

Pattern: hashing / frequency tracking
Complexity: O(n) average time, O(n) extra space

This is the optimised version: duplicate_set makes the 'already recorded'
check O(1). Checking `num not in duplicates` on the list instead would make
the worst case O(n^2).

Interview answers
1. Logical correctness: Yes | I keep a set of values seen so far. When a
   value appears again I record it as a duplicate, but only once.
2. Edge cases:
   - [1, 2, 3, 2, 4, 1] -> [2, 1]
   - [1, 2, 3] -> []
   - [5, 5, 5] -> [5]
   - [] -> []
   - [1, 1, 2, 2, 3, 3] -> [1, 2, 3]
3. Production ready: Yes, for a basic utility | O(n) average time and O(n)
   extra space. I'd clarify whether duplicates should follow the order of
   their first repeat (as here) or their original position.
"""


def find_duplicates(lst):
    seen = set()
    duplicates = []
    duplicate_set = set()

    for num in lst:
        if num in seen:
            if num not in duplicate_set:
                duplicates.append(num)
                duplicate_set.add(num)
        else:
            seen.add(num)

    return duplicates


print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))
# [2, 1]
