# 0-1 Knapsack problem with can have unlimited same items to choose
# Bruce force
# Time O(2^c) Space O(c)
# C is the capacity
def dfs(profit, weight, capacity):
    return dfsHelper(0, profit, weight, capacity)


def dfsHelper(i, profit, weight, capacity):
    if i == len(profit):
        return 0

    # not include i
    maxProfit = dfsHelper(i + 1, profit, weight, capacity)
    # include i
    newCapacity = capacity - weight[i]
    if newCapacity >= 0:
        # this is the diff with 0-1 problem, we can choose i again
        p = profit[i] + dfsHelper(i, profit, weight, newCapacity)
        maxProfit = max(maxProfit, p)

    return maxProfit


# Memorization
# Time O(n * m) Space O(n * m)
def memoization(profit, weight, capacity):
    N, M = len(profit), capacity
    cache = [[-1] * (M + 1) for _ in range(N)]
    return memoHelper(0, profit, weight, capacity, cache)


def memoHelper(i, profit, weight, capacity, cache):
    if i == len(profit):
        return 0
    if cache[i][capacity] != -1:
        return cache[i][capacity]

    # not include item i
    cache[i][capacity] = memoHelper(i + 1, profit, weight, capacity, cache)
    # include item i
    newCapacity = capacity - weight[i]
    if newCapacity >= 0:
        # here is the diff from 0-1
        p = profit[i] + memoHelper(i, profit, weight, newCapacity, cache)
        cache[i][capacity] = max(cache[i][capacity], p)

    return cache[i][capacity]

# dp
# Time and Space O(n * m)


def dp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # fill the edge case of the dp arrays
    for i in range(N):
        dp[i][0] = 0
    for c in range(M + 1):
        if c >= weight[0]:
            dp[0][c] = profit[0]

    for i in range(1, N):
        for c in range(1, M + 1):
            skip = dp[i - 1][c]
            # include
            if c - weight[i] >= 0:
                include = profit[i] + dp[i][c - weight[i]]
            else:
                include = 0
            dp[i][c] = max(include, skip)

    return [N - 1][M]


# Memory optimized dp
# Time O(n * m) Space O (m)
def optimizedDp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [0] * (M + 1)

    for i in range(N):
        curRow = [0] * (M + 1)
        for c in range(1, M + 1):
            skip = dp[c]
            include = 0
            if c - weight[i] >= 0:
                include = profit[i] + curRow[c - weight[i]]
            curRow[c] = max(include, skip)
        dp = curRow

    return dp[M]
# 这么来看的话0-1背包问题也可以优化空间，只需要两行就可以解决问题
