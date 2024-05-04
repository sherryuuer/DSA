# https://leetcode.com/problems/combinations/description/


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        curcomb = []

        def helper(i, curcomb, res, n, k):
            if len(curcomb) == k:
                res.append(curcomb[:])
                return
            if i > n:
                return

            curcomb.append(i)
            helper(i + 1, curcomb, res, n, k)
            curcomb.pop()

            helper(i + 1, curcomb, res, n, k)

        helper(1, curcomb, res, n, k)
        return res


class Solution_v2(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(start, curcomb):
            if len(curcomb) == k:
                res.append(curcomb[:])
                return
            for i in range(start, n + 1):
                curcomb.append(i)
                helper(i + 1, curcomb)
                curcomb.pop()

        helper(1, [])
        return res


n = 4
k = 2
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
solution = Solution()
res = solution.combine(n, k)
print(res)
