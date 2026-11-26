"""Snippet 27: Merge two sorted lists into one sorted list.

Pattern: two pointers / merge technique
Complexity: O(n + m) time, O(n + m) extra space

Same merge step that Merge Sort uses.

Interview answers
1. Logical correctness: Yes | I keep two pointers and compare the current
   elements of both sorted lists. I append the smaller one and move its
   pointer, then append whatever remains.
2. Edge cases:
   - [1, 3, 5], [2, 4, 6] -> [1, 2, 3, 4, 5, 6]
   - [1, 2], [3, 4] -> [1, 2, 3, 4]
   - [], [1, 2] -> [1, 2]
   - [1, 1], [1, 2] -> [1, 1, 1, 2]
   - [], [] -> []
3. Production ready: Yes, for sorted inputs | Takes O(n + m) time and O(n +
   m) extra space. I'd validate that both lists are sorted if the caller
   cannot guarantee it.
"""


def merge_sorted(a, b):
    i = 0
    j = 0
    merged = []

    while i < len(a) and j < len(b):

        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    while i < len(a):
        merged.append(a[i])
        i += 1

    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged


print(merge_sorted([1, 3, 5], [2, 4, 6]))
# [1, 2, 3, 4, 5, 6]
