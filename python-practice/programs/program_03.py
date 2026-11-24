"""Program 3: Identify duplicate elements in a list.

Example: [1, 2, 3, 2, 4, 1, 5] -> [1, 2]
(Duplicates are listed in the order their first copy appears.)

TC: O(n^2)
SC: O(d), d = number of duplicate values stored
Concept: nested loops / element comparison
Note: the already_exists flag makes sure an element is added only when a
later copy of it is found.
"""


def dup_ele(ele):
    dup = []
    for i in range(len(ele)):
        already_exists = False
        for j in range(i + 1, len(ele)):
            if ele[i] == ele[j]:
                already_exists = True
        if already_exists and ele[i] not in dup:
            dup.append(ele[i])
    return dup


ele = [1, 2, 3, 2, 4, 1, 5]
print(dup_ele(ele))
