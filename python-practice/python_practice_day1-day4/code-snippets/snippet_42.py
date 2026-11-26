"""Snippet 42: Calculate the mean of a list, handling an empty list safely.

Pattern: aggregation / running sum
Complexity: O(n) time, O(1) extra space

Mean = sum of all elements / number of elements.

Interview answers
1. Logical correctness: Yes | I check for an empty list first to avoid
   division by zero. Otherwise I add up the elements and divide by their
   count.
2. Edge cases:
   - [10, 20, 30, 40] -> 25.0
   - [5] -> 5.0
   - [1, 2] -> 1.5
   - [-5, 5] -> 0.0
   - [] -> None
3. Production ready: No | The calculation is correct, but production code
   should validate numeric inputs and decide whether NaN or infinity are
   acceptable.
"""


def calculate_mean(lst):
    if len(lst) == 0:
        return None

    total = 0

    for num in lst:
        total += num

    return total / len(lst)


print(calculate_mean([10, 20, 30, 40]))
# 25.0
