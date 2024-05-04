# https://leetcode.com/problems/container-with-most-water/description/
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# output = 49


class mySolution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        for L in range(len(height)):
            for R in range(L, len(height)):
                area = (R - L) * min(height[L], height[R])
                maxArea = max(maxArea, area)
        return maxArea
# 我就知道会被网友弄的超时


# 再想一次，几何知识袭来。
class mygoodSolution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L, R = 0, len(height) - 1
        curheight = min(height[L], height[R])
        maxArea = (R - L) * curheight
        while L < R:
            if height[L] <= curheight:
                while height[L] <= curheight and L < len(height) - 1:
                    L += 1
                curheight = min(height[L], height[R])
            else:
                while height[R] <= curheight and R > 0:
                    R -= 1
                curheight = min(height[L], height[R])
            maxArea = max(maxArea, (R - L) * curheight)
        return maxArea

# 过！打败了百分之九十八的网友！爽，更新两个隔板的时候，如果比最短的还短就直接跳过！


# 更新一下简化版本
# 但是其实它这个版本没有我的那个快，只有百分之六十的分数。
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L, R = 0, len(height) - 1
        maxArea = 0
        while L < R:
            maxArea = max(maxArea, (R - L) * min(height[L], height[R]))
            if height[L] <= height[R]:
                L += 1
            else:
                R -= 1
        return maxArea


height = [1, 2, 4, 3]
# output = 4

solution = Solution()
res = solution.maxArea(height)
print(res)
