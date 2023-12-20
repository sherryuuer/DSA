# https://leetcode.com/problems/combination-sum/description/
# import math
# candidates = [2, 3, 6, 7]
# target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# 每个数字num都可以出现0-n次当numxn超过了target就可以停下
candidates = [2, 3, 5]
target = 8


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        subset = []

        def dfs(idx):
            if sum(subset) == target:
                res.append(subset[:])
                return

            if idx >= len(candidates) or sum(subset) > target:
                return

            subset.append(candidates[idx])
            dfs(idx)

            subset.pop()
            dfs(idx + 1)

        dfs(0)

        return res


s = Solution()
res = s.combinationSum(candidates, target)
print(res)


####
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
