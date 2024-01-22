# https://leetcode.com/problems/min-cost-to-connect-all-points/description/


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        import heapq
        from collections import defaultdict
        n = len(points)

        adj = defaultdict(list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + \
                    abs(points[i][1] - points[j][1])
                adj[tuple(points[i])].append([tuple(points[j]), d])
                adj[tuple(points[j])].append([tuple(points[i]), d])
        print(adj)

        minheap = [[0, tuple(points[0])]]
        visit = set()
        res = 0
        while minheap and len(visit) < n:
            cost, v = heapq.heappop(minheap)
            if v in visit:
                continue
            visit.add(tuple(v))
            res += cost
            for neighbor, cost in adj[v]:
                if neighbor not in visit:
                    heapq.heappush(minheap, [cost, neighbor])
        return res


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
# Output: 20
solution = Solution()
res = solution.minCostConnectPoints(points)
print(res)


# 参考题解：因为其实点坐标在一开始就已经没用了，只需要符号表示和他们的权重边，所以一开始可以抽象化为索引即可。
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}  # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        res = 0
        visit = set()
        minH = [[0, 0]]  # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res
