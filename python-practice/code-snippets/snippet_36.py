"""Snippet 36: Implement bubble sort for a list of numbers.

Pattern: sorting / adjacent swapping
Complexity: O(n^2) average and worst case, O(n) best case (already sorted), O(1) extra space

Interview answers
1. Logical correctness: Yes | I compare adjacent elements and swap them when
   they are in the wrong order. After every pass the largest unsorted element
   is in its final place at the end.
2. Edge cases:
   - [5, 2, 8, 1, 3] -> [1, 2, 3, 5, 8]
   - [1, 2, 3] -> [1, 2, 3]
   - [5, 4, 3, 2] -> [2, 3, 4, 5]
   - [4, 4, 2, 2] -> [2, 2, 4, 4]
   - [] -> []
   - [-3, 5, -1] -> [-3, -1, 5]
3. Production ready: No | O(n^2) average and worst case. It is fine for
   learning, but in production I'd use Python's built-in sorting or a more
   efficient algorithm. It also sorts the input list in place.
"""


def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break

    return lst


print(bubble_sort([5, 2, 8, 1, 3]))
# [1, 2, 3, 5, 8]
