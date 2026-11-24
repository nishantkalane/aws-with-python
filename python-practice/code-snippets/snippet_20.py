"""Snippet 20: Check whether a number is a perfect number.

Pattern: divisor enumeration / mathematical logic
Complexity: O(sqrt(n)) time, O(1) extra space

A perfect number equals the sum of its proper divisors (excluding itself).
Example: 6 = 1 + 2 + 3.

Interview answers
1. Logical correctness: Yes | I calculate the sum of proper divisors and compare
   it with the number. I check divisor pairs only up to the square root to
   avoid unnecessary iterations.
2. Edge cases:
   6 -> True, 28 -> True, 12 -> False, 1 -> False, 0 -> False,
   negative number -> False
3. Production ready: Yes, for a basic utility | O(sqrt(n)) time and O(1) extra
   space. I'd validate the input type and define the acceptable input range.
"""


def is_perfect(n):
    if n <= 1:
        return False

    total = 1
    i = 2

    while i * i <= n:
        if n % i == 0:
            total += i

            if i != n // i:
                total += n // i

        i += 1

    return total == n


print(is_perfect(6))    # True
print(is_perfect(28))   # True
print(is_perfect(12))   # False
