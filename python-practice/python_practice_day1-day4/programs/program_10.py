"""Program 10: Rotate an array to the right by k positions.

Example: [1, 2, 3, 4, 5, 6, 7], k = 3 -> [5, 6, 7, 1, 2, 3, 4]

Approach: array reversal algorithm
  Original             [1, 2, 3, 4, 5, 6, 7]
  Reverse entire array [7, 6, 5, 4, 3, 2, 1]
  Reverse first k      [5, 6, 7, 4, 3, 2, 1]
  Reverse the rest     [5, 6, 7, 1, 2, 3, 4]

TC: O(n)
SC: O(1)
Concept: array manipulation / two pointers
Note: k = k % n handles k larger than the array length.
"""


def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def rotate_right(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    k = k % n

    # Step 1: reverse the entire array
    reverse(arr, 0, n - 1)
    # Step 2: reverse the first k elements
    reverse(arr, 0, k - 1)
    # Step 3: reverse the remaining elements
    reverse(arr, k, n - 1)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_right(arr, k))
