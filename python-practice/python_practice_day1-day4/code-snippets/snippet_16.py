"""Snippet 16: Calculate the least common multiple (LCM) of two integers.

Pattern: mathematical formula / GCD
Complexity: O(log n) time

Formula: LCM(a, b) = |a * b| / GCD(a, b). Reuses the GCD from snippet 15.

Interview answers
1. Logical correctness: Yes | I calculate the GCD first and use the
   GCD-LCM relationship to get the least common multiple. Zero inputs are
   handled separately to avoid division by zero.
2. Edge cases:
   lcm(12,18) -> 36, lcm(4,6) -> 12, lcm(5,7) -> 35, lcm(0,8) -> 0,
   lcm(-4,6) -> 12, lcm(0,0) -> 0
3. Production ready: Yes, for a basic utility | Efficient and handles negative
   and zero inputs. I'd add input validation and define the behaviour for
   invalid input types.
"""


def gcd(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


def lcm(a, b):
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


print(lcm(12, 18))  # 36
print(lcm(4, 6))    # 12
