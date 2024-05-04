# https://leetcode.com/problems/search-a-2d-matrix/description/
# Input:
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
# Output: true


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def searcharr(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                middle = (left + right) // 2
                if target < arr[middle]:
                    right = middle - 1
                elif target > arr[middle]:
                    left = middle + 1
                else:
                    return True
            return False

        # n = len(matrix)
        # for m in range(n):
        #     if target >= matrix[m][0] and target <= matrix[m][-1]:
        #         return searcharr(matrix[m], target)

        # 如果外层也用二分查找
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:  # important!! It's 0!
                bot = row - 1
            else:
                return searcharr(matrix[row], target)
        return False


solution = Solution()
res = solution.searchMatrix(matrix, target)
print(res)
