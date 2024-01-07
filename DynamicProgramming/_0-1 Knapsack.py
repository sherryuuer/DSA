# capacity of pack
# items with profit and weight
# max the profit

# bruce force
# Time O(2^n) Space O(n)
def dfs(profit, weight, capacity):
    return dfsHelper(0, profit, weight, capacity)


def dfsHelper(i, profit, weight, capacity):
    if i == len(profit):
        return 0

    # not include item i
    maxProfit = dfsHelper(i + 1, profit, weight, capacity)
    # include item i
    newCapacity = capacity - weight[i]
    if newCapacity >= 0:
        # here use the newCapacity
        p = profit[i] + dfsHelper(i + 1, profit, weight, newCapacity)
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
        # here use the newCapacity
        p = profit[i] + memoHelper(i + 1, profit, weight, newCapacity, cache)
        cache[i][capacity] = max(cache[i][capacity], p)

    return cache[i][capacity]


# dp
# Time O(n * m) Space O(n * m)
def dp(profit, weight, capacity):
    N, M = len(profit), capacity
    dp = [[0] * (M + 1) for _ in range(N)]

    # fill the edge case
    # all 0 so this is no need
    # for i in range(N):
    #     dp[i][0] = 0
    for c in range(M + 1):
        if c >= weight[0]:
            dp[0][c] = profit[0]

    for i in range(1, N):
        for c in range(1, M + 1):
            skip = dp[i - 1][c]
            # include case
            if c - weight[i] >= 0:
                include = profit[i] + dp[i - 1][c - weight[i]]
            else:
                include = 0
            # get the max profit
            dp[i][c] = max(include, skip)

    return dp[N - 1][M]
