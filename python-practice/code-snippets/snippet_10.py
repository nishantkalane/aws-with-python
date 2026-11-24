"""Snippet 10: Calculate the factorial of a non-negative integer iteratively.

Pattern: iteration / accumulator
Complexity: O(n) time

Interview answers
1. Logical correctness: Yes | I start the result at 1 and multiply it by every
   integer from 1 to n. 0! correctly returns 1.
2. Edge cases:
   5 -> 120, 1 -> 1, 0 -> 1, -3 -> None
3. Production ready: No | Correct for non-negative integers, but production
   code should validate the input type and raise an explicit error for invalid
   values instead of silently returning None.
"""


def factorial(n):
    if n < 0:
        return None

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(5))  # 120
print(factorial(0))  # 1
