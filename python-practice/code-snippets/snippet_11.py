"""Snippet 11: Calculate the nth Fibonacci number recursively.

Pattern: recursion
Complexity: O(2^n) time (exponential)

Sequence: 0, 1, 1, 2, 3, 5, 8, 13 ... each number is the sum of the previous two.

Interview answers
1. Logical correctness: Yes | I use base cases for 0 and 1, and for other
   values I add the previous two Fibonacci numbers, following the recurrence.
2. Edge cases:
   0 -> 0, 1 -> 1, 2 -> 1, 6 -> 8, negative input -> None
3. Production ready: No | The logic is correct, but this recursion repeats
   calculations and becomes very slow for larger inputs. For production I'd use
   memoization or an iterative approach.
"""


def fibonacci(n):
    if n < 0:
        return None

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))  # 8
