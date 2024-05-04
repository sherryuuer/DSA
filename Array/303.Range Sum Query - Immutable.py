# https://leetcode.com/problems/range-sum-query-immutable/description/


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
