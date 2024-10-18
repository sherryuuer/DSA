s = "anagram"
t = "nagaram"
# Output: true

s = "rat"
t = "car"
# Output: false
# anagram means one string is rerange by another string
# step:
# 1, Space O(1) so a dict is good to store the num of characters
# 2, loop s and t, add char num -> delete char num
# 3, if dict is empty true


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        from collections import defaultdict
        charDict = defaultdict(int)

        lenOfString = len(s)

        for i in range(lenOfString):
            charDict[s[i]] += 1
            charDict[t[i]] -= 1


        for value in charDict.values():
            if value != 0:
                return False
        return True


s = "anagram"
t = "nagaram"
solution = Solution()
res = solution.isAnagram(s, t)
print(res)
