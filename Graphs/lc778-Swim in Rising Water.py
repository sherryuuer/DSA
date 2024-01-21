# https://leetcode.com/problems/swim-in-rising-water/description/


# Dijkstra本质也是一种dfs，这道题要计算每个点到达的最小条件，也就是那条路上最大的height。
# 在每次更新中，都更新各个网格点的需要的最大高度即可
# 疑问是这道题能不能动态规划。
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import heapq
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))

        while minH:
            t, r, c = heapq.heappop(minH)
            visit.add((r, c))
            if r == N - 1 and c == N - 1:
                return t

            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if nr >= 0 and (nr <= N - 1) and nc >= 0 and (nc <= N - 1) and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])


grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [
    12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
# output = 16
