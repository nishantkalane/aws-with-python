"""Program 9: Find the majority element.

Find the element that appears more than n/2 times. If none, return None.
Example: [1, 1, 1, 2, 2, 1] -> 1

TC: O(n)
SC: O(1)
Concept: Boyer-Moore voting algorithm
Note: two phases:
  1. find a possible majority candidate
  2. verify it really occurs more than n/2 times
Finding a candidate does not guarantee a majority element exists.
"""


def majority_element(arr):
    candidate = None
    count = 0

    # Phase 1: find candidate
    for num in arr:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    # Phase 2: verify candidate
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None


arr = [1, 1, 1, 2, 2, 1]
print(majority_element(arr))
