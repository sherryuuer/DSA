# Design an algorithm to encode a list of strings to a single string.
# The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode.

strs = ["we","say",":","yes"]
# Output: ["we","say",":","yes"]

class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s

        return res

    def decode(self, s):
        length = len(s)

        res = []
        i = 0

        while i < length:
            j = i
            while s[j] != "#":
                j += 1
            lenOfcurStr = int(s[i: j])

            i = j + 1
            j = i + lenOfcurStr
            res.append(s[i:j])

            i = j

        return res


solution = Solution()
s = solution.encode(strs)
print(s)
res = solution.decode(s)
print(res)
