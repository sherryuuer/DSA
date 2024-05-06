class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for c in s:
            res = res ^ ord(c)
        for c in t:
            res = res ^ ord(c)
        return chr(res)


s = "abcd"
t = "abcde"
solution = Solution()
print(solution.findTheDifference(s, t))


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sum_s, sum_t = 0, 0
        for c in s:
            sum_s += ord(c)
        for c in t:
            sum_t += ord(c)

        return chr(sum_t - sum_s)


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        count_s, count_t = Counter(s), Counter(t)
        for c in count_t:
            if c not in count_s:
                return c
            if count_t[c] > count_s[c]:
                return c
