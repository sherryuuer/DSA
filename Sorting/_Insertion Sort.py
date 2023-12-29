# Definition for a pair.
# Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]

# Output:
# [[(5, "apple"), (2, "banana"), (9, "cherry")],
#  [(2, "banana"), (5, "apple"), (9, "cherry")],
#  [(2, "banana"), (5, "apple"), (9, "cherry")]]


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def insertionSort(self, pairs: list[Pair]) -> list[list[Pair]]:

        res = []
        for i in range(1, len(pairs)):
            j = i - 1
            while j > 0 and pairs[j][0] < pairs[j - 1][0]:
                tmp = pairs[j]
                pairs[j] = pairs[j - 1]
                pairs[j - 1] = tmp
                j -= 1
            res.append(pairs[:])
        return res


solution = Solution()
res = solution.insertionSort(pairs)
print(res)


# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
# class Solution:
#     # Implementation of Insertion Sort
#     def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
#         n = len(pairs)
#         res = []  # To store the intermediate states of the array

#         for i in range(n):
#             j = i - 1

#             # Move elements that are greater than key one position ahead
#             while j >= 0 and pairs[j].key > pairs[j + 1].key:
#                 pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
#                 j -= 1

#             # Clone and save the entire state of the array at this point
#             res.append(pairs[:])

#         return res
