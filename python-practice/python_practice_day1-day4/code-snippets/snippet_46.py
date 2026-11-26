"""Snippet 46: Compare two dictionaries and return the keys whose values differ.

Pattern: dictionary traversal / key comparison
Complexity: O(n) average time (n = keys in the first dictionary)

Assumption: only keys present in BOTH dictionaries are compared.

Interview answers
1. Logical correctness: Yes | I iterate through the first dictionary, check
   whether each key exists in the second, and compare the values. If they
   differ I add the key to the result.
2. Edge cases:
   - {"a": 1}, {"a": 2} -> ['a']
   - {"a": 1}, {"a": 1} -> []
   - {"a": 1, "b": 2}, {"a": 3, "b": 2} -> ['a']
   - {}, {} -> []
   - {"a": 1}, {"b": 2} -> [] (keys in only one dictionary are ignored)
3. Production ready: No | It ignores keys that exist in only one dictionary.
   In production I'd clarify whether a missing key counts as a difference and
   validate the inputs.
"""


def compare_dictionaries(dict1, dict2):
    differences = []

    for key in dict1:
        if key in dict2:
            if dict1[key] != dict2[key]:
                differences.append(key)

    return differences


a = {"name": "Nishant", "age": 23, "city": "Nagpur"}
b = {"name": "Nishant", "age": 24, "city": "Pune"}

print(compare_dictionaries(a, b))
# ['age', 'city']
