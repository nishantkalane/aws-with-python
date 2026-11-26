"""Snippet 39: Transpose a two-dimensional matrix.

Pattern: matrix traversal / row-column swapping
Complexity: O(r * c) time and space

Interview answers
1. Logical correctness: Yes | I traverse the matrix column by column,
   collecting the element from each row. Rows become columns, which gives the
   transposed matrix.
2. Edge cases:
   - [[1,2,3], [4,5,6]] -> [[1,4], [2,5], [3,6]]
   - [[1,2], [3,4]] -> [[1,3], [2,4]]
   - [[5]] -> [[5]]
   - [] -> []
   - [[1,2,3]] -> [[1], [2], [3]]
3. Production ready: No | Works for rectangular matrices but assumes every
   row has the same length. I'd add validation for empty and irregular
   matrices and clarify whether the original should be modified.
"""


def transpose(matrix):
    if len(matrix) == 0:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        new_row = []

        for i in range(rows):
            new_row.append(matrix[i][j])

        result.append(new_row)

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transpose(matrix))
# [[1, 4], [2, 5], [3, 6]]
