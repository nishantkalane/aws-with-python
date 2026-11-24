"""Program 2: Find the second-largest number in a list.

Example: [10, 20, 4, 45, 99] -> 45

TC: O(n)
SC: O(1)
Concept: two-variable tracking (no sorting, no max())
Note: finds the second-largest DISTINCT value. If all elements are equal,
it returns None.
"""


def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = arr[0]
    second = None

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num < largest:
            if second is None or num > second:
                second = num
    return second


arr = [10, 20, 4, 45, 99]
print(second_largest(arr))
