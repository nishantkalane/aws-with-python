"""Snippet 21: Count the frequency of each word in a sentence.

Pattern: hashing / frequency counting
Complexity: O(n) time

Interview answers
1. Logical correctness: Yes | I convert the sentence to lowercase, split it
   into words, and use a dictionary to count how often each word appears.
2. Edge cases:
   "hello world hello" -> hello: 2, "Python python" -> python: 2,
   "one" -> one: 1, empty sentence -> {}
3. Production ready: No | The basic logic is correct, but punctuation is not
   normalised, so "hello" and "hello," count as different words. I'd add text
   normalisation and define Unicode and tokenisation requirements.
"""


def word_frequency(sentence):
    freq = {}
    words = sentence.lower().split()

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


print(word_frequency("Python is easy and Python is powerful"))
# {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
