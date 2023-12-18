# https://leetcode.com/problems/first-bad-version/description/

# Input:
n = 5
bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:
            current = (low + high) // 2
            if not isBadVersion(current):
                low = current + 1
            elif isBadVersion(current):
                if not isBadVersion(current - 1):
                    return current
                else:
                    high = current - 1
