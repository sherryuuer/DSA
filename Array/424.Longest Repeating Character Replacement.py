# https://leetcode.com/problems/longest-repeating-character-replacement/description/
s = "ABAA"
k = 0
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# # first time solution time out for some big case
# class Solution(object):
#     def characterReplacement(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         def countv(lst):
#             from collections import Counter
#             elecounts = Counter(lst)
#             maxcount = max(elecounts.values())
#             return len(lst) - maxcount

#         if not s:
#             return 0
#         length = 1
#         L = 0

#         for R in range(len(s)):
#             while countv(s[L: R + 1]) > k:
#                 L += 1
#             length = max(R - L + 1, length)
#         return length


# optimize O
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0

        count = {}
        length = 0
        L = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            while (R - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1

            length = max(R - L + 1, length)
            # print(count, L, R, length)
        return length


solu = Solution()
res = solu.characterReplacement(s, k)
print(res)


# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         count = {}

#         l = 0
#         maxf = 0
#         for r in range(len(s)):
#             count[s[r]] = 1 + count.get(s[r], 0)
#             maxf = max(maxf, count[s[r]])

#             if (r - l + 1) - maxf > k:
#                 count[s[l]] -= 1
#                 l += 1

#         return (r - l + 1)
