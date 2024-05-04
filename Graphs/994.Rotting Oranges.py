# https://leetcode.com/problems/rotting-oranges/description/
grid = [[2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]]
# Output: 4
# 找到每一个好橘子，走到烂橘子的最长距离


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        m, n = len(grid), len(grid[0])

        def bfs(r, c):
            direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            visit = set((r, c))
            queue = deque()
            queue.append((r, c))
            minite = 0
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    if grid[r][c] == 2:
                        return minite
                    for dr, dc in direction:
                        nr, nc = r + dr, c + dc
                        if (min(nr, nc) < 0
                            or nr == m or nc == n
                            or grid[nr][nc] == 0
                                or (nr, nc) in visit):
                            continue
                        visit.add((nr, nc))
                        queue.append((nr, nc))
                minite += 1
            return -1

        minites = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    minite = bfs(r, c)
                    if minite == -1:
                        return -1
                    minites = max(minites, minite)
        return minites


solution = Solution()
res = solution.orangesRotting(grid)
print(res)


#####
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
