"""Snippet 40: Calculate the sum of the main diagonal of a square matrix.

Pattern: matrix traversal / diagonal traversal
Complexity: O(n) time, O(1) extra space

Main diagonal of the example is 1, 5, 9, so the sum is 15.

Interview answers
1. Logical correctness: Yes | I walk the matrix using the same row and column
   index. The main diagonal has equal row and column indices, so I add
   matrix[i][i] to the total.
2. Edge cases:
   - [[1,2,3], [4,5,6], [7,8,9]] -> 15
   - [[5]] -> 5
   - [[1,2], [3,4]] -> 5
   - [] -> 0
3. Production ready: No | Correct for square matrices, but it does not
   validate that the matrix is square. I'd add dimension checks and input
   type checks.
"""


def diagonal_sum(matrix):
    n = len(matrix)
    total = 0

    for i in range(n):
        total += matrix[i][i]

    return total


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(diagonal_sum(matrix))  # 15
