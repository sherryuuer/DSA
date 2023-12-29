# Input:
pairs = [(3, "cat"), (2, "dog"), (3, "bird")]

# Output:
# [(2, "dog"), (3, "bird"), (3, "cat")]

# Definition for a pair.


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def quickSort(self, pairs: list[Pair]) -> list[Pair]:
        n = len(pairs)
        if n <= 0:
            return pairs
        pivot = pairs[-1]
        left = 0
        for i in range(n - 1):
            if pairs[i].key < pivot.key:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1
        pairs[-1] = pairs[left]
        pairs[left] = pivot

        return self.quickSort(pairs[:left]) + [pivot] + self.quickSort(pairs[left + 1:])
