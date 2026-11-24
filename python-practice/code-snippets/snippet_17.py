"""Snippet 17: Calculate the sum of the digits of an integer.

Pattern: digit extraction (modulo and division)
Complexity: O(d) time, d = number of digits

  % 10  extracts the last digit
  // 10 removes the last digit

Interview answers
1. Logical correctness: Yes | I extract the last digit with modulo 10, add it
   to the total, and remove it with integer division by 10, repeating until the
   number becomes zero.
2. Edge cases:
   1234 -> 10, 567 -> 18, 1005 -> 6, 0 -> 0, -123 -> 6
3. Production ready: Yes, for a basic utility | Correct and O(d). I'd validate
   the input type and define how negative numbers should be treated.
"""


def sum_of_digits(n):
    n = abs(n)
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    return total


print(sum_of_digits(1234))  # 10
print(sum_of_digits(567))   # 18
