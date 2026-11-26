"""Snippet 12: Return the first n Fibonacci numbers.

Pattern: iteration with two variables
Complexity: O(n) time, O(n) space (the returned list)

The series is 0, 1, 1, 2, 3, 5, 8, ... Each number is the sum of the
previous two.

NOTE: this question was in your question list but missing from the
walkthrough file, so this solution was added separately in the same format.

Interview answers
1. Logical correctness: Yes | I keep two variables, a and b, starting at 0
   and 1. On each step I append a to the result and move forward with
   a, b = b, a + b. After n steps the list holds the first n Fibonacci
   numbers.
2. Edge cases:
   7 -> [0, 1, 1, 2, 3, 5, 8], 1 -> [0], 2 -> [0, 1], 0 -> [],
   negative n -> []
3. Production ready: Yes, for a basic utility | Linear time and avoids the
   repeated work of the recursive version. For production I'd validate that n
   is an integer and decide whether negative input should raise an error
   instead of returning an empty list. If n can be huge, a generator would
   avoid storing the whole list.
"""


def first_n_fibonacci(n):
    if n <= 0:
        return []

    series = []
    a, b = 0, 1

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


print(first_n_fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8]
print(first_n_fibonacci(1))  # [0]
