"""Snippet 7: Find the second-largest distinct number in a list.

Pattern: one-pass traversal / tracking
Complexity: O(n) time, O(1) space

Interview answers
1. Logical correctness: Yes | I maintain the largest and second-largest
   distinct values in one pass. Whenever a larger value is found, the previous
   largest becomes the second-largest.
2. Edge cases:
   [1,6,7,8,9,10] -> 9, [5,5,4] -> 4, [1,2] -> 1, [5,5,5] -> None, [] -> None
3. Production ready: No | Efficient at O(n), but production code should define
   how to handle empty lists, lists with fewer than two distinct values, and
   invalid input types.
"""


def second_largest(lst):
    if len(lst) < 2:
        return None

    largest = lst[0]
    second = None

    for i in range(1, len(lst)):
        if lst[i] > largest:
            second = largest
            largest = lst[i]

        elif lst[i] < largest:
            if second is None or lst[i] > second:
                second = lst[i]

    return second


print(second_largest([1, 6, 7, 8, 9, 10, 2]))
# 9
