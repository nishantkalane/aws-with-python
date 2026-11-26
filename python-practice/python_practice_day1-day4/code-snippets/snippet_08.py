"""Snippet 8: Find the smallest and largest numbers in one pass.

Pattern: one-pass traversal
Complexity: O(n) time, O(1) extra space

Note: do not initialise smallest/largest to 0, because an all-negative list
would give a wrong answer. Start from the first element.

Interview answers
1. Logical correctness: Yes | I initialise smallest and largest with the first
   element, then compare every remaining element to update them, all in one
   traversal.
2. Edge cases:
   [8,6,7,2,11] -> (2, 11), [-5,-2,-10] -> (-10, -2), [5,5,5] -> (5, 5),
   [7] -> (7, 7), [] -> None
3. Production ready: Yes, for a basic utility | Efficient. For production I'd
   add input validation and define the empty-list behaviour.
"""


def find_min_max(lst):
    if len(lst) == 0:
        return None

    smallest = lst[0]
    largest = lst[0]

    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]

        if lst[i] > largest:
            largest = lst[i]

    return smallest, largest


print(find_min_max([8, 6, 7, 2, 3, 11, 4]))
# (2, 11)
