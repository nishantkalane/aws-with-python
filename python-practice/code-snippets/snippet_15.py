"""Snippet 15: Calculate the greatest common divisor (GCD) of two integers.

Pattern: Euclidean algorithm
Complexity: O(log n) time

Note: same problem as snippet 13. Remember the key step: repeatedly take the
remainder and replace the two numbers.

Interview answers
1. Logical correctness: Yes | I repeatedly replace the first number with the
   second and the second with their remainder. When the remainder is zero, the
   remaining number is the GCD.
2. Edge cases:
   gcd(48,18) -> 6, gcd(12,8) -> 4, gcd(7,13) -> 1, gcd(-12,18) -> 6,
   gcd(10,0) -> 10, gcd(0,0) -> 0 (by this implementation's convention)
3. Production ready: Yes, for a basic utility | Efficient, with logarithmic
   time. I'd validate input types and explicitly define the behaviour for two
   zero inputs.
"""


def gcd(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


print(gcd(48, 18))  # 6
print(gcd(12, 8))   # 4
