# https://leetcode.com/problems/longest-common-subsequence/description/
# Input:
# 最长公共子序列问题
text1 = "abcde"
text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        # for r in range(1, n + 1):
        #     for c in range(1, m + 1):
        #         if text1[c - 1] == text2[r - 1]:
        #             dp[r][c] = dp[r - 1][c - 1] + 1
        #         else:
        #             dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
        # return dp[n][m]
        # print(dp)

        # or button up
        for r in range(n - 1, - 1, -1):
            for c in range(m - 1, -1, -1):
                if text1[c] == text2[r]:
                    dp[r][c] = dp[r + 1][c + 1] + 1
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        return dp[0][0]


solution = Solution()
res = solution.longestCommonSubsequence(text1, text2)
print(res)
