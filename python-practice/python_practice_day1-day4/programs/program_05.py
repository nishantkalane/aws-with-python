"""Program 5: Find all pairs whose sum equals a target.

Example: arr = [2, 4, 3, 5, 7, 8, 1], target = 9
Output: {(7, 2), (5, 4), (8, 1)}  (pair ordering may vary)

TC: O(n) average
SC: O(n)
Concept: hashing / complement technique
Note: instead of checking every pair, check whether the needed complement
has already appeared.
"""


def find_pairs(arr, target):
    seen = set()
    pairs = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.add((complement, num))
        seen.add(num)
    return pairs


arr = [2, 4, 3, 5, 7, 8, 1]
target = 9
result = find_pairs(arr, target)
print("Pairs:", result)
