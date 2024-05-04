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
        curMax = curMin = maxSum = minSum = nums[0]
        total = sum(nums)

        for n in nums[1:]:
            curMax = max(n, curMax + n)
            curMin = min(n, curMin + n)
            minSum = min(curMin, minSum)
            maxSum = max(curMax, maxSum)
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum


solution = Solution()
res = solution.maxSubarraySumCircular(nums)
print(res)
