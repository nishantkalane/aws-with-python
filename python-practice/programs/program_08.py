"""Program 8: Find the length of the longest consecutive sequence.

Given an unsorted list of integers, find the length of the longest run of
consecutive numbers WITHOUT sorting.
Example: [100, 4, 200, 1, 3, 2] -> 4  (the run is 1, 2, 3, 4)

TC: O(n) average
SC: O(n)
Concept: hashing / set
Note: start counting only when num - 1 is not present, so the same run is
never counted twice.
"""


def long_cons(arr):
    nums = set(arr)
    longest = 0

    for num in nums:
        # only start counting at the first element of a run
        if num - 1 not in nums:
            current = num
            count = 1

            while current + 1 in nums:
                current += 1
                count += 1

            longest = max(longest, count)
    return longest


arr = [100, 4, 200, 1, 3, 2]
print(long_cons(arr))
