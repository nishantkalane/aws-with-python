"""Snippet 35: Implement binary search on a sorted list.

Pattern: binary search / divide and conquer
Complexity: O(log n) time, O(1) extra space

low = start index, high = end index, mid = middle index.

Interview answers
1. Logical correctness: Yes | I compute the middle index and compare its
   element with the target. If the target is greater I search the right half,
   otherwise the left half, until I find it or the search space is empty.
2. Edge cases:
   - [10, 20, 30, 40, 50], target=30 -> 2
   - [10, 20, 30, 40, 50], target=10 -> 0
   - [10, 20, 30, 40, 50], target=50 -> 4
   - [10, 20, 30], target=25 -> -1
   - [5], target=5 -> 0
   - [], target=5 -> -1
3. Production ready: Yes, for sorted inputs | O(log n) time and O(1) extra
   space. I'd validate that the input is sorted, or make sure the caller
   guarantees it.
"""


def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid

        elif lst[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


print(binary_search([10, 20, 30, 40, 50, 60], 40))  # 3
print(binary_search([10, 20, 30, 40, 50], 25))      # -1
