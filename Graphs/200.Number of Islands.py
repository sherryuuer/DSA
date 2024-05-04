# https://leetcode.com/problems/number-of-islands/description/
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
# Output: 1


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0

        def helper(grid, r, c, visit):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == '0' or (r, c) in visit:
                return
            visit.add((r, c))
            helper(grid, r + 1, c, visit)
            helper(grid, r, c + 1, visit)
            helper(grid, r - 1, c, visit)
            helper(grid, r, c - 1, visit)
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    helper(grid, r, c, visit)
                    count += 1
        return count


solution = Solution()
res = solution.numIslands(grid)
print(res)


######
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands


# BFS Version
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r, c) not in visited:

                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
