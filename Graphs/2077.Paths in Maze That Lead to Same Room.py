from collections import defaultdict
from itertools import combinations


def number_of_paths(n, corridors):
    g = defaultdict(set)
    for a, b in corridors:
        g[a].add(b)
        g[b].add(a)

    res = 0
    for i in range(1, n + 1):
        for m, n in combinations(g[i], 2):
            if m in g[n]:
                res += 1
    return res // 3


n = 5
corridors = [[1, 2], [5, 2], [4, 1], [2, 4], [3, 1], [3, 4]]
res = number_of_paths(n, corridors)
print(res)
