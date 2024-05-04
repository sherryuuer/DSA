# https://leetcode.com/problems/longest-palindromic-substring/description/


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        if len(s) == 1:
            return s

        longest = ""
        for i in range(len(s)):
            odd_longest = expand_around_center(i, i)
            even_longest = expand_around_center(i, i + 1)
            if len(odd_longest) > len(longest):
                longest = odd_longest
            if len(even_longest) > len(longest):
                longest = even_longest

        return longest
