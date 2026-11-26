"""Snippet 43: Calculate the median of a list of numbers.

Pattern: sorting / middle element selection
Complexity: O(n log n) time, O(n) extra space

Odd count: the middle element. Even count: the average of the two middle
elements.

Interview answers
1. Logical correctness: Yes | I sort the list. With an odd count I return the
   middle element; with an even count I return the average of the two middle
   elements.
2. Edge cases:
   - [7, 2, 5, 1, 9] -> 5
   - [1, 2, 3, 4] -> 2.5
   - [10] -> 10
   - [5, 5, 5, 5] -> 5.0
   - [-5, -1, 2] -> -1
   - [] -> None
3. Production ready: Yes, for valid numeric inputs | Sorting gives O(n log n)
   time and O(n) space for the sorted copy. For very large data where only
   the median is needed, a selection algorithm can find it in expected O(n)
   time.
"""


def calculate_median(lst):
    if len(lst) == 0:
        return None

    arr = sorted(lst)
    n = len(arr)
    mid = n // 2

    if n % 2 == 1:
        return arr[mid]
    else:
        return (arr[mid - 1] + arr[mid]) / 2


print(calculate_median([7, 2, 5, 1, 9]))  # 5
print(calculate_median([1, 2, 3, 4]))     # 2.5
