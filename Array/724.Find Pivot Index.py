# https://leetcode.com/problems/find-pivot-index/description/
nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11


class Solution_notOK(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 因为不是有序数组，所以双指针不行！！！！
        L, R = 0, len(nums) - 1
        lsum, rsum = 0, 0
        while L < R:
            if lsum < rsum:
                L += 1
                lsum += nums[L - 1]
            elif lsum > rsum:
                R -= 1
                rsum += nums[R]
            else:
                if L + 1 == R - 1:
                    return L + 1
                lsum += nums[L]
                rsum += nums[R]
                L += 1
                R -= 1
        return -1


class Solution_v1(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix, postfix = [0] * len(nums), [0] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i - 1]
            postfix[-1 * i - 1] = postfix[-1 * i] + nums[-1 * i]
        # print(prefix, postfix)
        for i in range(len(prefix)):
            if prefix[i] == postfix[i]:
                return i
        return -1


# 相比较我的算出所有的前缀和后缀和，这个动态计算后缀和的更棒！学习了！
class Solution_v2(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            rightsum = total - leftsum - nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1


# 最终还是需要前缀和算法
# nums = [2, 1, -1]
solution = Solution_v2()
res = solution.pivotIndex(nums)
print(res)
