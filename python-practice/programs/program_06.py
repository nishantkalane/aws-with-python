"""Program 6: Find the longest substring without repeating characters.

Example: s = "abcabbb" -> ["abc", "bca", "cab"]
(Returns all unique substrings of the maximum length, not just one.)

TC: O(n^2) worst case, including substring creation and the duplicate
    check on results. The sliding-window processing alone is O(n).
SC: O(n) auxiliary, excluding the returned substrings
Concept: sliding window + set
Note: left moves forward whenever a repeated character is found, which
keeps the current window free of duplicates.
"""


def longest_sub(s):
    seen = set()
    left = 0
    max_length = 0
    result = []

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        current_length = right - left + 1
        substring = s[left:right + 1]

        if current_length > max_length:
            max_length = current_length
            result = [substring]
        elif current_length == max_length:
            if substring not in result:
                result.append(substring)
    return result


s = "abcabbb"
print(longest_sub(s))
