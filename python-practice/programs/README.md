# Programs (10)

Each file has the problem statement, example, complexity and key concept in a docstring at the top.

Run from this folder (program 7 reads `sample.txt`):

```bash
python program_01.py
```

| # | File | Problem | Pattern | TC | SC | Status |
|---|------|---------|---------|----|----|--------|
| 1 | [program_01.py](program_01.py) | Second non-repeating character | Hashing | O(n) | O(k) | Done |
| 2 | [program_02.py](program_02.py) | Second-largest number | Two variables | O(n) | O(1) | Done |
| 3 | [program_03.py](program_03.py) | Find duplicates in a list | Nested loops | O(n²) | O(d) | Done |
| 4 | [program_04.py](program_04.py) | Missing number from 1 to n | Sum formula | O(n) | O(1) | Done |
| 5 | [program_05.py](program_05.py) | Pairs with a target sum | Hashing / complement | O(n) avg | O(n) | Done |
| 6 | [program_06.py](program_06.py) | Longest substring without repeats | Sliding window | O(n²)* | O(n) | Done |
| 7 | [program_07.py](program_07.py) | Count lines, words, characters in a file | File handling | O(C) | O(L) | Done |
| 8 | [program_08.py](program_08.py) | Longest consecutive sequence | Hashing / set | O(n) avg | O(n) | Done |
| 9 | [program_09.py](program_09.py) | Majority element | Boyer-Moore voting | O(n) | O(1) | Done |
| 10 | [program_10.py](program_10.py) | Rotate array right by k | Reversal algorithm | O(n) | O(1) | Done |

\*Program 6: the sliding window itself is O(n); creating substrings and checking duplicate results makes the overall worst case O(n²).
