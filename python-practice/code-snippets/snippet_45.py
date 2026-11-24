"""Snippet 45: Convert a list of key-value pairs into a dictionary.

Pattern: hashing / dictionary construction
Complexity: O(n) average time, O(n) space

Interview answers
1. Logical correctness: Yes | I iterate through each key-value pair and
   assign the value to its key. If a key appears more than once, the latest
   value overwrites the earlier one.
2. Edge cases:
   - [('a', 1), ('b', 2)] -> {'a': 1, 'b': 2}
   - [('x', 10)] -> {'x': 10}
   - [] -> {}
   - [('a', 1), ('a', 5)] -> {'a': 5}
3. Production ready: Yes, for valid key-value pairs | O(n) average time for n
   pairs. I'd add validation for malformed pairs and make sure keys are
   hashable.
"""


def pairs_to_dictionary(pairs):
    result = {}

    for key, value in pairs:
        result[key] = value

    return result


pairs = [("name", "Nishant"), ("age", 23), ("city", "Nagpur")]

print(pairs_to_dictionary(pairs))
# {'name': 'Nishant', 'age': 23, 'city': 'Nagpur'}
