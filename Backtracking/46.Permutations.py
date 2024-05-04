# https://leetcode.com/problems/permutations/description/


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(i, nums):
            if i == len(nums):
                return [[]]
            res = []
            perms = helper(i + 1, nums)
            for p in perms:
                for j in range(len(p) + 1):
                    pcopy = p[:]
                    pcopy.insert(j, nums[i])
                    res.append(pcopy)
            return res
        return helper(0, nums)


nums = [1, 2, 3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
solution = Solution()
res = solution.permute(nums)
print(res)
