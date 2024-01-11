# https://leetcode.com/problems/minimum-size-subarray-sum/description/


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        length = float("inf")
        total = 0
        L = 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L += 1

        return length if length != float("inf") else 0
