"""Snippet 9: Return all even numbers from a list.

Pattern: filtering / traversal
Complexity: O(n) time

Interview answers
1. Logical correctness: Yes | I traverse the list and check each number with
   the modulo operator. If the remainder after dividing by 2 is zero, I add it
   to the result.
2. Edge cases:
   [1,2,3,4] -> [2,4], [1,3,5] -> [], [-2,-4,3] -> [-2,-4], [0,2] -> [0,2],
   [] -> []
3. Production ready: Yes, for a basic utility | Straightforward, readable and
   O(n). For production I'd validate the input if only numeric lists are
   allowed.
"""


def get_even_numbers(lst):
    even = []

    for num in lst:
        if num % 2 == 0:
            even.append(num)

    return even


print(get_even_numbers([9, 2, 5, 6, 7, 8, 9, 10]))
# [2, 6, 8, 10]
