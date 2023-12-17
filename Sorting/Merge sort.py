# Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry"),
         (1, "date"), (9, "elderberry")]

# Output:
# [(1, "date"), (2, "banana"), (5, "apple"), (9, "cherry"), (9, "elderberry")]

# Definition for a pair.


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def mergeSort(self, pairs: list[Pair]) -> list[Pair]:
        def merge(left, right):
            res = []
            li = 0
            ri = 0
            while li < len(left) and ri < len(right):
                if left[li].key <= right[ri].key:
                    res.append(left[li])
                    li += 1
                else:
                    res.append(right[ri])
                    ri += 1
            return res + left[li:] + right[ri:]

        if len(pairs) <= 1:
            return pairs
        m = len(pairs) // 2
        left = pairs[:m]
        right = pairs[m:]

        return merge(self.mergeSort(left), self.mergeSort(right))
