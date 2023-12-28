# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
grid = [[0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]]
# Output: 4
grid2 = [[1, 0, 0],
         [1, 1, 0],
         [1, 1, 0]]
# -1
grid3 = [[0, 1, 1, 0, 0, 0],
         [0, 1, 0, 1, 1, 0],
         [0, 1, 1, 0, 1, 0],
         [0, 0, 0, 1, 1, 0],
         [1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 0]]
# 14
grid4 = [[1]]


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        n = len(grid)
        visit = set()
        visit.add((0, 0))
        queue = deque()
        queue.append((0, 0))
        length = 1
        directions = [[0, 1], [1, 0], [1, 1], [0, -1],
                      [-1, 0], [-1, -1], [1, -1], [-1, 1]]

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if (
                    min(r, c) < 0
                    or max(r, c) == n
                    or grid[r][c] == 1
                ):
                    continue
                if r == n - 1 and c == n - 1:
                    return length

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (
                        min(nr, nc) < 0
                        or nr == n
                        or nc == n
                        or grid[nr][nc] == 1
                        or (nr, nc) in visit
                    ):
                        continue
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        return -1


solution = Solution()
res = solution.shortestPathBinaryMatrix(grid4)
print(res)


###
class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        from collections import deque
        N = len(grid)
        q = deque([(0, 0, 1)])  # r, c, length
        visit = set((0, 0))
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while q:
            r, c, length = q.popleft()
            if (min(r, c) < 0 or max(r, c) >= N or
                    grid[r][c]):
                continue
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in direct:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
        return -1
