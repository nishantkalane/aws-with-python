"""Snippet 24: Find the longest common prefix among a list of strings.

Pattern: prefix matching / vertical scanning
Complexity: O(S) time, S = total characters examined across the strings

Example: ["flower", "flow", "flight"] -> "fl". Compare the characters at the
same index across all strings.

Interview answers
1. Logical correctness: Yes | I take each character of the first string and
   compare it with the character at the same position in every other string.
   On a mismatch I return the prefix collected so far.
2. Edge cases:
   ["flower","flow","flight"] -> "fl", ["dog","racecar","car"] -> "",
   ["apple","application"] -> "appl", ["hello"] -> "hello",
   ["","abc"] -> "", [] -> ""
3. Production ready: Yes, for a basic utility | Efficient and stops at the
   first mismatch. I'd validate input types and define whether comparisons are
   case-sensitive.
"""


def longest_common_prefix(words):
    if len(words) == 0:
        return ""

    for i in range(len(words[0])):

        char = words[0][i]

        for word in words:
            if i >= len(word) or word[i] != char:
                return words[0][:i]

    return words[0]


print(longest_common_prefix(["flower", "flow", "flight"]))
# fl

print(longest_common_prefix(["dog", "racecar", "car"]))
# "" (empty string)
