# https://leetcode.com/problems/valid-palindrome/description/
s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join(char for char in s if char.isalpha()
                    or char.isdigit()).lower()
        L, R = 0, len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True


solution = Solution()
res = solution.isPalindrome(s)
print(res)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        return (new == new[::-1])
