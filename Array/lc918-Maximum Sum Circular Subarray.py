# https://leetcode.com/problems/maximum-sum-circular-subarray/description/
nums = [5, -3, 5]
# Output: 10
# Formally, the next element of nums[i] is nums[(i + 1) % n]
# nums[2] next nums[3 % 3]
# and the previous element of nums[i] is nums[(i - 1 + n) % n].


class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = nums[0]
        L, R = 0, 1
        while True:
            if R == L:
                break

            if curSum + nums[R] < nums[R]:
                L = R
                curSum = nums[R]
            else:
                curSum = curSum + nums[R]

            maxSum = max(curSum, maxSum)
            R = (R + 1) % len(nums)
        return maxSum


solution = Solution()
res = solution.maxSubarraySumCircular(nums)
print(res)
