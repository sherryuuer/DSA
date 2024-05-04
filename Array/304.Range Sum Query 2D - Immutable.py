# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
# 计算面积问题算法是sum[r2, c2] - sum[r1-1, c2] - sum[r2, c1 - 1] + sum[r1 - 1, c1 - 1]
# 感觉用字典存储更快

class NumMatrix_v1(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        M, N = len(matrix), len(matrix[0])
        print(M, N)
        self.prefix = {}

        total = 0
        for c in range(N):
            total += matrix[0][c]
            self.prefix[(0, c)] = total

        for r in range(1, M):
            curtotal = 0
            for c in range(N):
                curtotal += matrix[r][c]
                self.prefix[(r, c)] = self.prefix[(r - 1, c)] + curtotal

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.prefix[(row2, col2)]
        elif row1 == 0 and col1 > 0:
            return self.prefix[(row2, col2)] - self.prefix[(row2, col1 - 1)]
        elif row1 > 0 and col1 == 0:
            return self.prefix[(row2, col2)] - self.prefix[(row1 - 1, col2)]
        return self.prefix[(row2, col2)] - self.prefix[(row1 - 1, col2)] - self.prefix[(row2, col1 - 1)] + self.prefix[(row1 - 1, col1 - 1)]


# 超出界限的时候，添加辅助的行列真的很方便
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        M, N = len(matrix), len(matrix[0])
        self.prefix = [[0] * (N + 1) for i in range(M + 1)]

        for r in range(1, M + 1):
            curtotal = 0
            for c in range(1, N + 1):
                curtotal += matrix[r - 1][c - 1]
                self.prefix[r][c] = self.prefix[r - 1][c] + curtotal

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.prefix[row2][col2] - self.prefix[row1 - 1][col2] - self.prefix[row2][col1 - 1] + self.prefix[row1 - 1][col1 - 1]


matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
    1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(matrix)
print(obj.prefix)
param_1 = obj.sumRegion(row1=2, col1=1, row2=4, col2=3)
