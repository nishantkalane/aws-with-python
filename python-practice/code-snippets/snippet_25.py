"""Snippet 25: Check whether brackets in a string are balanced.

Pattern: stack / LIFO
Complexity: O(n) time, O(n) extra space

The last opened bracket must be the first one closed, so we use a stack.
  ({[]}) -> balanced
  ([)]   -> not balanced
Remember: append(), stack[-1], pop().

Interview answers
1. Logical correctness: Yes | I push opening brackets onto a stack. For every
   closing bracket I check that the top of the stack is its matching opening
   bracket, then remove it. At the end the stack must be empty.
2. Edge cases:
   "({[]})" -> True, "([)]" -> False, "{[]}" -> True, "(((" -> False,
   ")))" -> False, "" -> True, "abc" -> True (non-bracket characters ignored)
3. Production ready: Yes, for a basic utility | O(n) time and O(n) extra space.
   I'd clarify whether non-bracket characters should be ignored or rejected.
"""


def is_balanced(s):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:

        if char in "({[":
            stack.append(char)

        elif char in ")}]":

            if len(stack) == 0:
                return False

            if stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


print(is_balanced("({[]})"))  # True
print(is_balanced("([)]"))    # False
print(is_balanced("{[]}"))    # True
