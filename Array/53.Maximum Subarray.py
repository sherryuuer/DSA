# https://leetcode.com/problems/maximum-subarray/description/
# Input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = nums[0]

        for n in nums[1:]:
            curSum = max(curSum + n, n)
            maxSum = max(maxSum, curSum)
        return maxSum
