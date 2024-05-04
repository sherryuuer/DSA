# https://leetcode.com/problems/max-area-of-island/description/

grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        max_area = 0

        def helper(grid, r, c, visit):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r, c) in visit:
                return 0

            visit.add((r, c))
            area = 1
            area += helper(grid, r + 1, c, visit)
            area += helper(grid, r, c + 1, visit)
            area += helper(grid, r - 1, c, visit)
            area += helper(grid, r, c - 1, visit)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = helper(grid, r, c, visit)
                    max_area = max(max_area, area)
        return max_area


solution = Solution()
res = solution.maxAreaOfIsland(grid)
print(res)


####
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
