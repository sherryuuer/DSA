# https://leetcode.com/problems/partition-equal-subset-sum/description/


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            newDp = set()
            for t in dp:
                if t == target:
                    return True
                newDp.add(t)
                newDp.add(t + nums[i])
            dp = newDp
        return False


nums = [1, 5, 11, 5]
# Output: true
solution = Solution()
res = solution.canPartition(nums)
print(res)

# 尝试暴力破解
