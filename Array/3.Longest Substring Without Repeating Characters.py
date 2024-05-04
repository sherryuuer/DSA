# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        length = 1
        L = 0
        for R in range(len(s)):
            while s[R] in s[L:R]:
                L += 1
            length = max(R - L + 1, length)
        return length


solution = Solution()
res = solution.lengthOfLongestSubstring(s)
print(res)
