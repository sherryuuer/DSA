# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# binary search
# nums[M] >= nums[L] means left side is sorted so min is at right

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        L, R = 0, len(nums) - 1
        while L < R and nums[L] > nums[R]:
            M = (L + R) // 2
            if nums[M] >= nums[L]:
                L = M + 1
            else:
                R = M

        return nums[L]


nums1 = [3, 4, 5, 1, 2]
nums2 = [11, 12, 13, 14]
nums3 = [4, 5, 6, 7, 0, 1, 2]
nums4 = [3, 1, 2]
solution = Solution()
print(solution.findMin(nums1))
print(solution.findMin(nums2))
print(solution.findMin(nums3))
print(solution.findMin(nums4))
