"""Snippet 13: Check whether a number is prime.

Pattern: trial division
Complexity: O(sqrt(n)) time

A prime number is greater than 1 and has exactly two factors: 1 and itself.

Interview answers
1. Logical correctness: Yes | I check the number is greater than 1, then test
   divisors from 2 upward. If any divides it exactly it is not prime,
   otherwise it is prime.
2. Edge cases:
   2 -> True, 7 -> True, 9 -> False, 1 -> False, 0 -> False, -5 -> False
3. Production ready: Yes, for a basic utility | Correct, and checks divisors
   only up to the square root using i * i <= n. For production I'd add input
   validation and consider a stronger algorithm for extremely large numbers.
"""


def is_prime(n):
    if n <= 1:
        return False

    i = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += 1

    return True


print(is_prime(7))   # True
print(is_prime(10))  # False
