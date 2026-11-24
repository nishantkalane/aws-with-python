"""Snippet 34: Implement linear search: return the index of the target, or -1.

Pattern: linear search / sequential traversal
Complexity: O(n) time, O(1) extra space

Interview answers
1. Logical correctness: Yes | I traverse the list from the start and compare
   each element with the target. On a match I return its index, otherwise -1.
2. Edge cases:
   - [10, 20, 30], target=20 -> 1
   - [10, 20, 30], target=50 -> -1
   - [5, 5, 5], target=5 -> 0 (first match)
   - [7], target=7 -> 0
   - [], target=5 -> -1
3. Production ready: Yes, for a basic utility | Correct, and works on sorted
   and unsorted lists. O(n) time and O(1) extra space.
"""


def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i

    return -1


print(linear_search([10, 20, 30, 40], 30))  # 2
print(linear_search([10, 20, 30, 40], 50))  # -1
