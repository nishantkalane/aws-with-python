"""Snippet 19: Check whether a number is an Armstrong number.

Pattern: digit extraction / mathematical logic
Complexity: O(d) time, d = number of digits

An Armstrong number equals the sum of its digits, each raised to the power of
the number of digits. Example: 153 = 1^3 + 5^3 + 3^3.

Interview answers
1. Logical correctness: Yes | I first count the digits, then extract each digit
   and raise it to the power of the digit count. If the sum equals the original
   number, it is an Armstrong number.
2. Edge cases:
   153 -> True, 370 -> True, 9474 -> True, 123 -> False, 0 -> True,
   -153 -> False
3. Production ready: Yes, for a basic utility | Correct and O(d). I'd add input
   validation and consider the cost of large integer exponentiation.
"""


def is_armstrong(n):
    if n < 0:
        return False

    temp = n
    digits = 0

    if temp == 0:
        digits = 1
    else:
        while temp > 0:
            digits += 1
            temp //= 10

    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n


print(is_armstrong(153))   # True
print(is_armstrong(9474))  # True
print(is_armstrong(123))   # False
