# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtracking(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for c in digitToChar[digits[i]]:
                backtracking(i + 1, cur + c)
        if digits:
            backtracking(0, "")
        return res


digits = "23"
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]
solution = Solution()
res = solution.letterCombinations(digits)
print(res)
