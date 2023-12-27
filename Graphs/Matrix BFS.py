from collections import deque

# Matrix (2D grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]


# Shortest path from top left to bottom right
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    length = 0
    queue = deque()
    queue.append((0, 0))
    visit = set()
    visit.add((0, 0))

    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            steps = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for sr, sc in steps:
                if min(r + sr, c + sc) < 0 or r + sr == ROWS or c + sc == COLS or (r + sr, c + sc) in visit or grid[r + sr][c + sc] == 1:
                    continue
                queue.append((r + sr, c + sc))
                visit.add((r + sr, c + sc))
        length += 1


print(bfs(grid))
