"""Snippet 37: Find the top k largest values in a list.

Pattern: repeated maximum selection
Complexity: O(k * n) time, O(n) extra space (copy of the list)

Returns the top k values in descending order, duplicates included. Works on a
copy, so the input list is not changed.

Interview answers
1. Logical correctness: Yes | I repeatedly find the largest remaining
   element, add it to the result and remove it from consideration. Repeating
   this k times gives the k largest values in descending order.
2. Edge cases:
   - [4, 1, 7, 3, 9], k=3 -> [9, 7, 4]
   - [5, 5, 3, 2], k=2 -> [5, 5]
   - [1, 2, 3], k=1 -> [3]
   - [1, 2, 3], k=0 -> []
   - [], k=0 -> []
   - k > len(lst) -> None
3. Production ready: No | O(k * n) time, and removing elements adds overhead.
   In production I'd use a min-heap of size k (O(n log k)) via
   heapq.nlargest, or just sort when that is simpler.
"""


def top_k_largest(lst, k):
    if k < 0 or k > len(lst):
        return None

    arr = lst.copy()
    result = []

    for i in range(k):
        largest = arr[0]
        largest_index = 0

        for j in range(1, len(arr)):
            if arr[j] > largest:
                largest = arr[j]
                largest_index = j

        result.append(largest)
        arr.pop(largest_index)

    return result


print(top_k_largest([4, 1, 7, 3, 9, 2], 3))
# [9, 7, 4]
