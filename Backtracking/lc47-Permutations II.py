# https://leetcode.com/problems/permutations-ii/description/


class Solution_recursive(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(i, nums):
            if i == len(nums):
                return [[]]
            res = []
            perm = helper(i + 1, nums)
            for p in perm:
                for j in range(len(p) + 1):
                    pcopy = p[:]
                    pcopy.insert(j, nums[i])
                    if pcopy not in res:
                        res.append(pcopy)
            print(res)
            return res
        return helper(0, nums)

# backtracking


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import Counter

        counter = Counter(nums)

        res = []
        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for n in counter:
                if counter[n] > 0:
                    perm.append(n)
                    counter[n] -= 1
                    print(perm, counter)
                    dfs()
                    perm.pop()
                    counter[n] += 1
        dfs()
        return res


nums = [1, 1, 2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
solution = Solution()
res = solution.permuteUnique(nums)
print(res)
