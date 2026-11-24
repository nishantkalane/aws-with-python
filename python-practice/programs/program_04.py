"""Program 4: Find the missing number from 1 to n.

A list contains the numbers 1 to n with exactly one number missing.
Example: [1, 2, 3, 5, 6] -> 4

TC: O(n)
SC: O(1)
Concept: mathematical formula
    Sum = n * (n + 1) / 2
    Missing = expected sum - actual sum
Note: assumes positive integers from 1 to n, one missing, no duplicates.
"""


def missing_no(arr):
    n = len(arr) + 1
    total_actual = n * (n + 1) // 2
    total_secondary = sum(arr)
    missing = total_actual - total_secondary
    return missing


arr = [1, 2, 3, 5, 6]
print(missing_no(arr))
