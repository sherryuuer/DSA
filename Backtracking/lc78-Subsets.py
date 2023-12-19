# https://leetcode.com/problems/subsets/description/
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# backtracking问题，每个num都决定要不要加入，二叉树问题2^n
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subset = []

        def dfs(idx):
            if idx >= len(nums):
                res.append(subset[:])
                return

            # include the idx num
            subset.append(nums[idx])
            dfs(idx + 1)
            # not include the idx num
            subset.pop()
            dfs(idx + 1)
        dfs(0)
        return res
