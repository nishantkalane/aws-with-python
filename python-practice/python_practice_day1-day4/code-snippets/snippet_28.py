"""Snippet 28: Move all zeros to the end, preserving the order of other items.

Pattern: two pointers / in-place modification
Complexity: O(n) time, O(1) auxiliary space

pos tracks where the next non-zero element should go.

Interview answers
1. Logical correctness: Yes | I use a pointer to place every non-zero element
   at the front of the list in its original order. Then I fill the remaining
   positions with zeros.
2. Edge cases:
   - [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
   - [0, 0, 0] -> [0, 0, 0]
   - [1, 2, 3] -> [1, 2, 3]
   - [0, 0, 5] -> [5, 0, 0]
   - [] -> []
3. Production ready: Yes, for a basic utility | O(n) time and O(1) auxiliary
   space because it modifies the original list. I'd clarify whether modifying
   the input list is acceptable.
"""


def move_zeros(lst):
    pos = 0

    for i in range(len(lst)):
        if lst[i] != 0:
            lst[pos] = lst[i]
            pos += 1

    while pos < len(lst):
        lst[pos] = 0
        pos += 1

    return lst


print(move_zeros([0, 1, 0, 3, 12]))
# [1, 3, 12, 0, 0]
