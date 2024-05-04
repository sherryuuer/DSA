# https://leetcode.com/problems/palindromic-substrings/description/


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def expand_around_center(left, right):
            c = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                c += 1
                left -= 1
                right += 1
            return c

        count = 0
        for i in range(len(s)):
            count += expand_around_center(i, i)
            count += expand_around_center(i, i + 1)
        return count
