# 最长公共子串，不需要连续
# s1, s2 longest common subsequence
# base case end with out of index

# Time O(2^(n + m)) Space O(n + m)
def dfs(s1, s2):
    return dfsHelper(s1, s2, 0, 0)


def dfsHelper(s1, s2, l1, l2):
    if l1 == len(s1) or l2 == len(s2):
        return 0

    if s1[l1] == s2[l2]:
        return 1 + dfsHelper(s1, s2, l1 + 1, l2 + 1)
    else:
        return max(dfsHelper(s1, s2, l1 + 1, l2),
                   dfsHelper(s1, s2, l1, l2 + 1))


# Memorization
# Time O(n * m) Space O(n + m)
def memoization(s1, s2):
    N, M = len(s1), len(s2)
    cache = [[-1] * M for _ in range(N)]
    return memoHelper(s1, s2, 0, 0, cache)


def memoHelper(s1, s2, l1, l2, cache):
    if l1 == len(s1) or l2 == len(s2):
        return 0
    if cache[l1][l2] != -1:
        return cache[l1][l2]

    if s1[l1] == s2[l2]:
        cache[l1][l2] = 1 + memoHelper(s1, s2, l1 + 1, l2 + 1, cache)
    else:
        cache[l1][l2] = max(memoHelper(s1, s2, l1 + 1, l2, cache),
                            memoHelper(s1, s2, l1, l2 + 1, cache))
    return cache[l1][l2]


# dp
# Time O(n * m) Space O(n + m)
def dp(s1, s2):
    N, M = len(s1), len(s2)
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(M):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[N][M]


# dp-optimized
# Time O(n * m) Space O(m)
def optimizedDp(s1, s2):
    N, M = len(s1), len(s2)
    dp = [0] * (M + 1)

    for i in range(N):
        curRow = [0] * (M + 1)
        for j in range(M):
            if s1[i] == s2[j]:
                curRow[j + 1] = dp[j] + 1
            else:
                curRow[j + 1] = max(dp[j + 1], curRow[j])
        dp = curRow
    return dp[M]

# 最长公共子序列， 需要连续
# 对角线加一问题
