"""Snippet 14: Return all prime numbers up to n.

Pattern: nested traversal / trial division
Complexity: O(n * sqrt(n)) time

Interview answers
1. Logical correctness: Yes | I check every number from 2 to n for
   divisibility. If a number has no divisor other than 1 and itself, I add it
   to the result list.
2. Edge cases:
   20 -> [2,3,5,7,11,13,17,19], 10 -> [2,3,5,7], 2 -> [2], 1 -> [], 0 -> [],
   negative input -> []
3. Production ready: Yes, for moderate inputs | Correct, with a square-root
   optimisation per number. For larger inputs I'd use the Sieve of
   Eratosthenes for better performance.
"""


def primes_up_to(n):
    primes = []

    for num in range(2, n + 1):
        is_prime = True

        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            primes.append(num)

    return primes


print(primes_up_to(20))
# [2, 3, 5, 7, 11, 13, 17, 19]
