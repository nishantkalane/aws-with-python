"""Snippet 31: Find the missing number in a list of distinct values from 1 to n.

Pattern: mathematics / summation
Complexity: O(n) time, O(1) extra space

Missing = n(n+1)/2 - actual sum.

Interview answers
1. Logical correctness: Yes | I calculate the expected sum of 1 to n and
   subtract the sum of the given list. The difference is the missing number.
2. Edge cases:
   - [1, 2, 4, 5], n=5 -> 3
   - [2, 3, 4, 5], n=5 -> 1
   - [1, 2, 3, 4], n=5 -> 5
   - [2], n=2 -> 1
   - [1], n=2 -> 2
3. Production ready: No | Efficient, but it assumes exactly one number is
   missing and every other value is distinct and within range. I'd validate
   these assumptions.
"""


def missing_number(lst, n):
    expected = n * (n + 1) // 2
    actual = 0

    for num in lst:
        actual += num

    return expected - actual


print(missing_number([1, 2, 4, 5], 5))  # 3
