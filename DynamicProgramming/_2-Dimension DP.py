# Brute Force O(2 ^ (n + m))
def bruteForce(r, c, rows, cols):
    if r == rows or c == cols:
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1
    return bruteForce(r, c + 1, rows, cols) + bruteForce(r + 1, c, rows, cols)


res = bruteForce(0, 0, 4, 4)


# Memoization O(n * m))
def memoization(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    if cache[r][c] > 0:
        return cache[r][c]
    if r == rows - 1 and c == cols - 1:
        return 1

    cache[r][c] = bruteForce(r, c + 1, rows, cols, cache) + \
        bruteForce(r + 1, c, rows, cols, cache)
    return cache[r][c]


res = bruteForce(0, 0, 4, 4, [[0] * 4 for i in range(4)])


# Dynamic Programming - Time: O(n * m), Space: O(m), where m is num of cols
def dp(rows, cols):
    preRow = [0] * cols

    for row in range(rows - 1, -1, -1):
        curRow = [0] * cols
        curRow[cols - 1] = 1
        for c in range(cols - 2, -1, -1):
            curRow[c] = curRow[c + 1] + preRow[c]
        preRow = curRow
    return preRow[0]


res = dp(4, 4)
