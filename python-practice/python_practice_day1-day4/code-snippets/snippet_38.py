"""Snippet 38: Merge overlapping intervals.

Pattern: sorting / greedy algorithm
Complexity: O(n log n) time (sorting), O(n) space

CHANGE FROM THE SOURCE: the original updated the caller's own inner lists in
place, so after calling it on [[1,3],[2,6]] the input had become
[[1,6],[2,6]]. This version copies each interval first, so the input stays
untouched.

Interview answers
1. Logical correctness: Yes | I sort the intervals by start point, then
   compare each one with the last merged interval. If they overlap I extend
   its end, otherwise I add a new interval.
2. Edge cases:
   - [[1,3], [2,6], [8,10]] -> [[1,6], [8,10]]
   - [[1,4], [4,5]] -> [[1,5]]
   - [[1,2], [3,4]] -> [[1,2], [3,4]]
   - [[1,5]] -> [[1,5]]
   - [] -> []
   - [[1,10], [2,3], [4,5]] -> [[1,10]]
3. Production ready: Yes, for valid interval inputs | O(n log n) time because
   of sorting, O(n) space for the result. I'd validate the interval structure
   and that each start is not greater than its end.
"""


def merge_intervals(intervals):
    if len(intervals) == 0:
        return []

    intervals = sorted(intervals, key=lambda x: x[0])

    # copy each interval so the caller's lists are not modified
    merged = [intervals[0][:]]

    for i in range(1, len(intervals)):
        last = merged[-1]

        if intervals[i][0] <= last[1]:
            last[1] = max(last[1], intervals[i][1])
        else:
            merged.append(intervals[i][:])

    return merged


print(merge_intervals([[1, 3], [2, 6], [8, 10], [9, 12]]))
# [[1, 6], [8, 12]]
