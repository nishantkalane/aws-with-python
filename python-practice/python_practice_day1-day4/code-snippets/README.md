# Code Snippets (50)

Interview-style snippets: you are shown a piece of code and asked three things.

1. Is it logically correct?
2. What are the edge cases?
3. Is it production ready?

Each file has the problem, pattern, complexity and these three answers in a docstring at the top, followed by the code.

Run any snippet with `python snippet_01.py`.

| # | File | Problem | Pattern | Status |
|---|------|---------|---------|--------|
| 1 | [snippet_01.py](snippet_01.py) | Reverse a string without slicing | Reverse traversal | Done |
| 2 | [snippet_02.py](snippet_02.py) | Palindrome check, ignoring case | Two pointers | Done |
| 3 | [snippet_03.py](snippet_03.py) | Count vowels | Traversal / counting | Done |
| 4 | [snippet_04.py](snippet_04.py) | Character frequency | Hashing | Done |
| 5 | [snippet_05.py](snippet_05.py) | Anagram check | Frequency counting | Done |
| 6 | [snippet_06.py](snippet_06.py) | Remove duplicates, keep order | Membership checking | Done |
| 7 | [snippet_07.py](snippet_07.py) | Second-largest distinct number | One-pass tracking | Done |
| 8 | [snippet_08.py](snippet_08.py) | Smallest and largest in one pass | One-pass traversal | Done |
| 9 | [snippet_09.py](snippet_09.py) | All even numbers | Filtering | Done |
| 10 | [snippet_10.py](snippet_10.py) | Factorial (iterative) | Accumulator | Done |
| 11 | [snippet_11.py](snippet_11.py) | nth Fibonacci (recursive) | Recursion | Done |
| 12 | [snippet_12.py](snippet_12.py) | First n Fibonacci numbers | Iteration | Done |
| 13 | [snippet_13.py](snippet_13.py) | Prime check | Trial division | Done |
| 14 | [snippet_14.py](snippet_14.py) | All primes up to n | Trial division | Done |
| 15 | [snippet_15.py](snippet_15.py) | GCD | Euclidean algorithm | Done |
| 16 | [snippet_16.py](snippet_16.py) | LCM | GCD + formula | Done |
| 17 | [snippet_17.py](snippet_17.py) | Sum of digits | Digit extraction | Done |
| 18 | [snippet_18.py](snippet_18.py) | Reverse digits of an integer | Digit extraction | Done |
| 19 | [snippet_19.py](snippet_19.py) | Armstrong number | Digit extraction | Done |
| 20 | [snippet_20.py](snippet_20.py) | Perfect number | Divisor enumeration | Done |
| 21 | [snippet_21.py](snippet_21.py) | Word frequency | Hashing | Done |
| 22 | [snippet_22.py](snippet_22.py) | First non-repeating character | Frequency counting | Done |
| 23 | [snippet_23.py](snippet_23.py) | Longest word in a sentence | Maximum tracking | Done |
| 24 | [snippet_24.py](snippet_24.py) | Longest common prefix | Vertical scanning | Done |
| 25 | [snippet_25.py](snippet_25.py) | Balanced brackets | Stack / LIFO | Done |
| 26 | [snippet_26.py](snippet_26.py) | Common elements between two lists | Hashing | Done |
| 27 | [snippet_27.py](snippet_27.py) | Merge two sorted lists | Two pointers | Done |
| 28 | [snippet_28.py](snippet_28.py) | Move zeros to the end | Two pointers / in-place | Done |
| 29 | [snippet_29.py](snippet_29.py) | Rotate a list right by k | Reversal algorithm | Done |
| 30 | [snippet_30.py](snippet_30.py) | Pairs with a target sum | Hashing / complement | Done |
| 31 | [snippet_31.py](snippet_31.py) | Missing number from 1 to n | Summation formula | Done |
| 32 | [snippet_32.py](snippet_32.py) | All duplicate values | Hashing | Done |
| 33 | [snippet_33.py](snippet_33.py) | Is the list sorted? | Adjacent comparison | Done |
| 34 | [snippet_34.py](snippet_34.py) | Linear search | Sequential search | Done |
| 35 | [snippet_35.py](snippet_35.py) | Binary search | Divide and conquer | Done |
| 36 | [snippet_36.py](snippet_36.py) | Bubble sort | Adjacent swapping | Done |
| 37 | [snippet_37.py](snippet_37.py) | Top k largest values | Repeated max selection | Done |
| 38 | [snippet_38.py](snippet_38.py) | Merge overlapping intervals | Sorting / greedy | Done |
| 39 | [snippet_39.py](snippet_39.py) | Transpose a matrix | Matrix traversal | Done |
| 40 | [snippet_40.py](snippet_40.py) | Main diagonal sum | Diagonal traversal | Done |
| 41 | [snippet_41.py](snippet_41.py) | Flatten a one-level nested list | Nested loop | Done |
| 42 | [snippet_42.py](snippet_42.py) | Mean (empty list safe) | Aggregation | Done |
| 43 | [snippet_43.py](snippet_43.py) | Median | Sorting | Done |
| 44 | [snippet_44.py](snippet_44.py) | Group words by first letter | Hashing / grouping | Done |
| 45 | [snippet_45.py](snippet_45.py) | Key-value pairs to dict | Dict construction | Done |
| 46 | [snippet_46.py](snippet_46.py) | Compare two dicts, keys that differ | Dict traversal | Done |
| 47 | [snippet_47.py](snippet_47.py) | Count lines, words, characters of a file | File handling | Done |
| 48 | [snippet_48.py](snippet_48.py) | Pandas: head, columns, dtypes of a CSV | Pandas inspection | Done |
| 49 | [snippet_49.py](snippet_49.py) | Pandas: missing counts + drop duplicates | Pandas cleaning | Done |
| 50 | [snippet_50.py](snippet_50.py) | Pandas: average purchase per city | Pandas groupby | Done |

## Notes

- Snippet 38 differs from the original: the original changed the caller's own interval lists, so it now copies each interval first.
- Snippet 32 uses the optimised version (a set to record duplicates).
- Snippets 48 to 50 need pandas (`pip install -r requirements.txt`). Snippet 48's demo uses an in-memory CSV because `*.csv` files are git-ignored.
- Snippet 47 reads `sample.txt` from this folder.
