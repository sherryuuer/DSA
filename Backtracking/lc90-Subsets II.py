# https://leetcode.com/problems/subsets-ii/description/


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        curset = []

        def dfs(i):
            if i >= len(nums):
                res.append(curset[:])
                return

            # include the i num
            curset.append(nums[i])
            dfs(i + 1)
            # backtracking, not include i num
            curset.pop()
            # find the first not dup num i
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res


nums = [1, 2, 2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
solution = Solution()
res = solution.subsetsWithDup(nums)
print(res)
