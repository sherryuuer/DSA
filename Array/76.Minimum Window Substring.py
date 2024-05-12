# https://leetcode.com/problems/minimum-window-substring/description/

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import copy
        n = len(s)
        charDict = {}
        for c in t:
            if c not in charDict:
                charDict[c] = 0
            charDict[c] += 1

        start = -1  # 记录最小窗口子序列的起始位置
        minLen = float('inf')  # 记录最小窗口子序列的长度

        i = 0
        dict1 = copy.deepcopy(charDict)
        while i < n:
            if s[i] in dict1:

                dict1[s[i]] -= 1  # 在字典中查看是否有该字符进行-1操作
                if dict1[s[i]] == 0:
                    del dict1[s[i]]

                if not dict1:  # 字典中的元素在S中都找到了
                    end = i  # 记录当前窗口的结束位置
                    # 重置字典用于寻找start
                    dict2 = copy.deepcopy(charDict)
                    while dict2:
                        if s[i] in dict2:
                            dict2[s[i]] -= 1
                            if dict2[s[i]] == 0:
                                del dict2[s[i]]
                        i -= 1
                    i += 1  # 退回到满足条件的位置

                    # 计算当前窗口子串的长度，并更新最小窗口的起始位置和长度
                    if end - i + 1 < minLen:
                        minLen = end - i + 1
                        start = i

                    # 这里很重要，要把dict1重制，以便下一次遍历和比较
                    dict1 = copy.deepcopy(charDict)
            i += 1

        if start == -1:
            return ""
        else:
            return s[start: start + minLen]


# 然后力扣网友又让我超时了。。。。只能优化看看
class Solution2(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import copy
        n = len(s)
        m = len(t)
        start = left = -1
        charDict = {}
        for c in t:
            if c not in charDict:
                charDict[c] = 0
            charDict[c] += 1

        minLen = float('inf')  # 记录最小窗口子序列的长度

        i = 0
        dict1 = copy.deepcopy(charDict)
        while i < n:
            if s[i] in dict1:

                dict1[s[i]] -= 1  # 在字典中查看是否有该字符进行-1操作
                if dict1[s[i]] == 0:
                    del dict1[s[i]]
                if left == -1:
                    left = i

                if not dict1:  # 字典中的元素在S中都找到了
                    end = i  # 记录当前窗口的结束位置
                    print(left, end)

                    # 计算当前窗口子串的长度，并更新最小窗口的起始位置和长度
                    if end - left + 1 < minLen:
                        minLen = end - left + 1
                        start = left

                    # 在重置left前重置i
                    i = left
                    # 这里很重要，要把dict1,left重制，以便下一次遍历和比较
                    dict1 = copy.deepcopy(charDict)
                    left = -1

            i += 1

        if start == -1:
            return ""
        else:
            return s[start: start + minLen]


# 然后力扣网友又让我超时了。。。。只能优化看看
class Solution3(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        m = len(t)
        start = left = -1
        charDict = {}
        for c in t:
            if c not in charDict:
                charDict[c] = 0
            charDict[c] += 1

        minLen = float('inf')  # 记录最小窗口子序列的长度
        i = 0
        checkDict = {}
        count = 0
        while i < n:
            if s[i] in charDict:
                if s[i] not in checkDict:
                    checkDict[s[i]] = 0

                if checkDict[s[i]] < charDict[s[i]]:
                    checkDict[s[i]] += 1
                    count += 1

                if left == -1:
                    left = i

                if count == m:  # 字典中的元素在S中都找到了
                    end = i  # 记录当前窗口的结束位置

                    # 计算当前窗口子串的长度，并更新最小窗口的起始位置和长度
                    if end - left + 1 < minLen:
                        minLen = end - left + 1
                        start = left

                    # 在重置left前重置i
                    i = left
                    # 这里很重要，要把dict1,left重制，以便下一次遍历和比较
                    left = -1
                    checkDict = {}
                    count = 0

            i += 1

        if start == -1:
            return ""
        else:
            return s[start: start + minLen]


# 然后力扣网友又让我超时了。。。。只能优化看看
class Solution4(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        m = len(t)
        start = left = -1
        charDict = {}
        for c in t:
            if c not in charDict:
                charDict[c] = 0
            charDict[c] += 1

        minLen = float('inf')  # 记录最小窗口子序列的长度
        i = 0
        checkDict = {}
        count = 0
        while i < n:
            if s[i] in charDict:
                if s[i] not in checkDict:
                    checkDict[s[i]] = 0

                if checkDict[s[i]] < charDict[s[i]]:
                    checkDict[s[i]] += 1
                    count += 1

                if left == -1:
                    left = i

                # 如果当前的长度已经比最小记录大了那没必要算了就！
                if i - left + 1 >= minLen:
                    i = left
                    # 这里很重要，要把dict1,left重制，以便下一次遍历和比较
                    left = -1
                    checkDict = {}
                    count = 0

                elif count == m:  # 字典中的元素在S中都找到了，并且小于最小记录
                    end = i  # 记录当前窗口的结束位置
                    minLen = end - left + 1
                    start = left

                    # 在重置left前重置i
                    i = left
                    # 这里很重要，要把dict1,left重制，以便下一次遍历和比较
                    left = -1
                    checkDict = {}
                    count = 0

            i += 1

        if start == -1:
            return ""
        else:
            return s[start: start + minLen]


# claude solution
class Solution_claude:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 如果目标字符串为空,直接返回空字符串
        if not t:
            return ""

        # 记录目标字符串中每个字符的出现次数
        target = {}
        for char in t:
            target[char] = target.get(char, 0) + 1

        # 初始化左右指针和最小窗口
        left, right = 0, 0
        min_window = ""
        min_len = float('inf')

        # 记录当前窗口中每个字符的出现次数
        window = {}

        # 记录当前窗口中包含目标字符串中所有字符的个数
        matched = 0

        while right < len(s):
            # 扩展右边界
            char = s[right]
            if char in target:
                window[char] = window.get(char, 0) + 1
                if window[char] == target[char]:
                    matched += 1

            # 缩小左边界
            while matched == len(target):
                # 更新最小窗口
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right+1]

                # 移动左指针
                left_char = s[left]
                if left_char in target:
                    window[left_char] -= 1
                    if window[left_char] < target[left_char]:
                        matched -= 1
                left += 1

            right += 1

        return min_window


s = "ADOBECODEBANC"
t = "ABC"

solution = Solution_claude()
res = solution.minWindow(s, t)
print(res)
