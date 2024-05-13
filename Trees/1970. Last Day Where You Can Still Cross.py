# https://leetcode.com/problems/last-day-where-you-can-still-cross/description/

class Solution:
    def latestDayToCross(self, row, col, cells):
        n = row * col
        # root是根节点，每个节点都指向自己，left和right是最左和最右边界
        root, left, right = list(range(n)), [0] * n, [0] * n

        # 使用格子索引更新左右边界的列表，所谓边界是指格子所在位置的col
        for i in range(col):
            for j in range(row):
                # [0, 0, 1, 1]
                left[i * row + j] = i
                right[i * row + j] = i

        # find找到根节点
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        # 合并连通分量，返回左右边界
        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                root[a] = b
            left[b] = min(left[b], left[a])
            right[b] = max(right[b], right[a])

        # 开始搜索
        seen = set()
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1),
                (1, 1), (-1, 1), (1, -1), (-1, -1))

        for i, cell in enumerate(cells):
            cx, cy = cell[0] - 1, cell[1] - 1
            for dx, dy in dirs:
                x, y = cx + dx, cy + dy
                # 检查相邻格子的有效性和是否见过
                if 0 <= x < row and 0 <= y < col and (x, y) in seen:
                    # union两个格子
                    union(cy * row + cx, y * row + x)
                    # 找到合并后的根节点
                    new = find(y * row + x)
                    # 检查新的组合是否可以跨越边界
                    if left[new] == 0 and right[new] == col - 1:
                        # 为真则返回天数
                        return i
            seen.add((cx, cy))

        return n


row = 2
col = 2
cells = [[1, 1], [2, 1], [1, 2], [2, 2]]
solution = Solution()
solution.latestDayToCross(row, col, cells)
