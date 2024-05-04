# https://leetcode.com/problems/unique-paths-ii/description/
# Input:
obstacleGrid = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
# Output: 2
# obstacleGrid = [[0, 0],
#                 [0, 1]]

# 第一次做的


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        preRow = obstacleGrid[-1]
        if preRow[-1] == 1:
            return 0
        preRow[-1] = 1
        for c in range(col - 2, -1, -1):
            if preRow[c] == 1:
                preRow[c] = 0
            else:
                preRow[c] = preRow[c + 1]

        for r in range(row - 2, -1, -1):
            curRow = [0] * col
            curRow[col - 1] = 1
            # 如何末尾是1或者下面一行是0
            if obstacleGrid[r][col - 1] == 1 or preRow[col - 1] == 0:
                curRow[col - 1] = 0

            for c in range(col - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                else:
                    curRow[c] = curRow[c + 1] + preRow[c]

            preRow = curRow

        return preRow[0]


solution = Solution()
res = solution.uniquePathsWithObstacles(obstacleGrid)
print(res)


# 但是其实动态规划这里只需要一行的空间
class Solution_dp(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[cols - 1] = 1

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < cols:
                    dp[c] = dp[c] + dp[c + 1]

        return dp[0]


class Solution_bruteForce(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(rows - 1, cols - 1): 1}

        def dfs(r, c):
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]

        return dfs(0, 0)
