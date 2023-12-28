# https://leetcode.com/problems/house-robber/description/
nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # rob = max(rob[0] + rob[2:], rob[1:])
        # [rob1, rob2, n, n + 1, n + 2, ...]
        # [0, 0, 1, 2, 3, 1]
        # [rob1, rob2, n,....]
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(rob1 + n, rob2)  # tmp = max(0 + 1, 0) = 1
            rob1 = rob2  # rob1 = 0
            rob2 = tmp  # rob2 = 1 the max
        return rob2


solution = Solution()
res = solution.rob(nums)
print(res)
