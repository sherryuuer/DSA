# 最长子回文
# 双指针问题
# 动态规划问题
# 一个字符串S返回里面的最长回文串
def longest(s):
    length = 0
    for i in range(len(s)):
        # odd length
        L, R = i, i
        while L >= 0 and R < len(s) and s[L] == s[R]:
            if (R - L + 1) > length:
                length = R - L + 1
            L -= 1
            R += 1
        # even length
        L, R = i, i + 1
        while L >= 0 and R < len(s) and s[L] == s[R]:
            if (R - L + 1) > length:
                length = R - L + 1
            L -= 1
            R += 1
    return length


s = "abaab"
res = longest(s)
print(res)


# 以上也是中心扩展法（llm）
def longestPalindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) == 1:
        return s

    longest = ""
    for i in range(len(s)):
        palindrome_odd = expand_around_center(i, i)
        palindrome_even = expand_around_center(i, i + 1)

        if len(palindrome_odd) > len(longest):
            longest = palindrome_odd
        if len(palindrome_even) > len(longest):
            longest = palindrome_even

    return longest


s = "abaab"
res = longestPalindrome(s)
print(res)


# dp
def longestPalindrome_dp(s):
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_len = i, 2

    # Check substrings of length 3 or more
    for length in range(3, n + 1):
        # 长度为length的子串的起始位置i
        for i in range(n - length + 1):
            # 结束位置j
            j = i + length - 1
            # 如果内部子串是回文，那么只需要判断两端
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                start, max_len = i, length

    return s[start:start + max_len]


res = longestPalindrome_dp(s)
print(res)
# [[True,  False, True,  False, False],
#  [False, True,  False, False, True],
#  [False, False, True,  True,  False],
#  [False, False, False, True,  False],
#  [False, False, False, False, True]]
