"""Snippet 30: Find all pairs in a list whose sum equals a target.

Pattern: hashing / complement search
Complexity: O(n) average time, O(n) extra space

complement = target - current number.

Interview answers
1. Logical correctness: Yes | I calculate the complement needed to reach the
   target and check whether it has already been visited. If it has, I record
   the pair and continue.
2. Edge cases:
   - [2, 4, 3, 5, 7], target=9 -> (4, 5), (2, 7)
   - [1, 1, 2, 2], target=3 -> (1, 2)
   - [3, 3], target=6 -> (3, 3)
   - [1, 2, 3], target=10 -> []
   - [], target=5 -> []
3. Production ready: Yes, for unique value pairs | O(n) average time with
   O(n) extra space. I'd clarify whether the requirement is unique value
   pairs or every index pair, especially when duplicates exist.
"""


def target_pairs(lst, target):
    seen = set()
    pairs = []
    added = set()

    for num in lst:
        complement = target - num

        if complement in seen:
            pair = (complement, num)

            if pair not in added:
                pairs.append(pair)
                added.add(pair)

        seen.add(num)

    return pairs


print(target_pairs([2, 4, 3, 5, 7, 8, 1], 9))
# [(4, 5), (2, 7), (8, 1)]
