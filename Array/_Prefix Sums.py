# prefix前缀和
# postfix后缀和
# Given an array of values, design a data structure that can query
# the sum of a subarray of the values
# 用subarray终点+1的前缀和减去开始的前缀和
class PrefixSum:

    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)
