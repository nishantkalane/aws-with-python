"""Snippet 18: Reverse the digits of an integer.

Pattern: digit extraction / mathematical manipulation
Complexity: O(d) time, d = number of digits

Same idea as snippet 17, but instead of adding the digit we build a new
reversed number.

Interview answers
1. Logical correctness: Yes | I extract the last digit and append it to the
   reversed number by multiplying the result by 10 and adding the digit,
   repeating until all digits are processed.
2. Edge cases:
   1234 -> 4321, 1005 -> 5001, -123 -> -321, 7 -> 7, 0 -> 0, 1200 -> 21
3. Production ready: No | The basic logic is correct, but production code
   should validate input types and handle integer overflow in fixed-width
   languages. Python integers do not have that fixed-width overflow limit.
"""


def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)

    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return sign * reverse


print(reverse_number(1234))   # 4321
print(reverse_number(567))    # 765
print(reverse_number(-123))   # -321
