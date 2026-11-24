"""Snippet 29: Rotate a list to the right by k positions.

Pattern: array manipulation / reversal algorithm
Complexity: O(n) time, O(1) auxiliary space

[1, 2, 3, 4, 5], k=2: reverse all -> [5, 4, 3, 2, 1]; reverse first k -> [4,
5, 3, 2, 1]; reverse the rest -> [4, 5, 1, 2, 3].

Interview answers
1. Logical correctness: Yes | I first reverse the entire list, then reverse
   the first k elements and the remaining elements separately. This produces
   a right rotation by k positions.
2. Edge cases:
   - [1, 2, 3, 4, 5], k=2 -> [4, 5, 1, 2, 3]
   - [1, 2, 3], k=1 -> [3, 1, 2]
   - [1, 2, 3], k=3 -> [1, 2, 3]
   - [1, 2, 3], k=5 -> [2, 3, 1]
   - [], k=2 -> []
   - [1], k=10 -> [1]
3. Production ready: Yes, for a basic utility | O(n) time and O(1) auxiliary
   space. I'd validate that k is an integer and clarify whether modifying the
   original list is acceptable.
"""


def rotate_right(lst, k):
    n = len(lst)

    if n == 0:
        return lst

    k = k % n

    def reverse(left, right):
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return lst


print(rotate_right([1, 2, 3, 4, 5], 2))
# [4, 5, 1, 2, 3]
