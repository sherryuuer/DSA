# Given n numbers (1 - n), return all possible combinations
# of size k. (n choose k math problem).
# Time: O(k * 2^n)
def combinations(n, k):
    combs = []
    curcomb = []
    helper(1, curcomb, combs, n, k)
    return combs


def helper(i, curcomb, combs, n, k):
    if len(curcomb) == k:
        combs.append(curcomb.copy())
        return
    if i > n:
        return

    # include i
    curcomb.append(i)
    helper(i + 1, curcomb, combs, n, k)
    curcomb.pop()
    # not include i
    helper(i + 1, curcomb, combs, n, k)


# Time O(k * C(n, k)) 使用排列组合公式优化
def combinations2(n, k):
    combs = []
    curcomb = []
    helper(1, curcomb, combs, n, k)
    return combs


def helper2(i, curcomb, combs, n, k):
    if len(curcomb) == k:
        combs.append(curcomb.copy())
        return
    if i > n:
        return

    for j in range(i, n + 1):
        curcomb.append(j)
        helper(j + 1, curcomb, combs, n, k)
        curcomb.pop()
