"""Snippet 41: Flatten a list nested exactly one level deep.

Pattern: nested loop / list traversal
Complexity: O(n) time, O(n) space (n = total items)

Interview answers
1. Logical correctness: Yes | I use two loops. The outer loop visits each
   inner list and the inner loop adds its elements to the result.
2. Edge cases:
   - [[1, 2], [3, 4]] -> [1, 2, 3, 4]
   - [[1], [2], [3]] -> [1, 2, 3]
   - [[], [1, 2], []] -> [1, 2]
   - [] -> []
   - [[], []] -> []
3. Production ready: No | Assumes every element is an iterable sublist. I'd
   validate the input structure and define how mixed or non-list elements
   should be handled.
"""


def flatten_list(lst):
    result = []

    for sublist in lst:
        for item in sublist:
            result.append(item)

    return result


print(flatten_list([[1, 2], [3, 4], [5, 6]]))
# [1, 2, 3, 4, 5, 6]
