# https://leetcode.com/problems/unique-paths/description/
# Input:
m = 3
n = 7
# Output: 28


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        preRow = [0] * n
        for row in range(m - 1, -1, -1):
            curRow = [0] * n
            curRow[n - 1] = 1
            for c in range(n - 2, -1, -1):
                curRow[c] = curRow[c + 1] + preRow[c]
            preRow = curRow
        return preRow[0]


solution = Solution()
res = solution.uniquePaths(m, n)
print(res)


###
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

        # O(n * m) O(n)
