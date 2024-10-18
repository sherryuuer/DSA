strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# steps:
# 1, if empty return []
# 2, res = [] going to store [] in it
# 3, loop strings list, find box for the string


class Solution:

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if len(s) == 0 and len(t) == 0:
            return True

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

    def groupAnagrams(self, strs):

        res = []
        if not strs: return res

        for str in strs:
            if not res:
                res.append([str,])
                continue

            foundList = False

            for strList in res:
                if self.isAnagram(strList[0], str):
                    strList.append(str)
                    foundList = True
                    break

            if not foundList:
                res.append([str,])

        return res


from collections import Counter

class Solution:

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

    def groupAnagrams(self, strs):
        res = {}

        for str_ in strs:
            # Sort the string to get the key that uniquely identifies an anagram group
            key = tuple(sorted(str_))
            print(key) # ('a', 'e', 't')

            if key not in res:
                res[key] = []
            res[key].append(str_)

        return list(res.values())


solution = Solution()
res = solution.groupAnagrams(strs)
print(res)
