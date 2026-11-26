"""Snippet 33: Determine whether a list is sorted in ascending order.

Pattern: linear traversal / adjacent comparison
Complexity: O(n) time, O(1) extra space

Interview answers
1. Logical correctness: Yes | I compare every element with the next one. If
   any element is greater than the next, the list is not sorted in ascending
   order.
2. Edge cases:
   - [1, 2, 3, 4] -> True
   - [1, 3, 2, 4] -> False
   - [1, 1, 2, 3] -> True
   - [5] -> True
   - [] -> True
   - [5, 4, 3] -> False
3. Production ready: Yes, for a basic utility | O(n) time and O(1) extra
   space. I'd clarify whether ascending allows duplicate values, since this
   implementation does.
"""


def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False

    return True


print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4]))     # False
