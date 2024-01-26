# https://leetcode.com/problems/distinct-subsequences/description/


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # cache = {}

        # def dfs(i, j):
        #     if j == len(t):
        #         return 1
        #     if i == len(s):
        #         return 0

        #     if (i, j) in cache:
        #         return cache[(i, j)]

        #     if s[i] == s[j]:
        #         cache[(i, j)] = dfs(i + 1, j) + dfs(i + 1, j + 1)
        #     else:
        #         cache[(i, j)] = dfs(i + 1, j)
        #     return cache[(i, j)]
        # return dfs(0, 0)

        m, n = len(s), len(t)

        # dp[i][j] 表示 s[:i] 中包含 t[:j] 的子序列个数
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 空串是任何字符串的子序列，因此 dp[i][0] 都为 1
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果当前字符相等，可以选择匹配或者不匹配
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # 如果当前字符不相等，只能选择不匹配
                    dp[i][j] = dp[i - 1][j]

        return dp  # dp[m][n]


s = "babgbag"
t = "bag"
# Output: 5
solution = Solution()
res = solution.numDistinct(s, t)
print(res)

[[1, 0, 0, 0],
 [1, 1, 0, 0],
 [1, 1, 1, 0],
 [1, 2, 1, 0],
 [1, 2, 1, 1],
 [1, 3, 1, 1],
 [1, 3, 4, 1],
 [1, 3, 4, 5]]
