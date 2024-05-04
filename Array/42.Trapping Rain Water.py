# https://leetcode.com/problems/trapping-rain-water/description/
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# output = 6


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        L, R = 0, len(height) - 1
        maxL, maxR = height[L], height[R]
        res = 0
        while L < R:
            if maxL < maxR:
                L += 1
                maxL = max(maxL, height[L])
                res += maxL - height[L]
            else:
                R -= 1
                maxR = max(maxR, height[R])
                res += maxR - height[R]

        return res


# 这个解法也是骚气的很
# 左右指针，更新较小的那个，储存左右指针的最大值，公式min(maxL, maxR) - height[i]
# 很棒的题
