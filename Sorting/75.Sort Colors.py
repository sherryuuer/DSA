# https://leetcode.com/problems/sort-colors/description/

# nums = [2, 0, 2, 1, 1, 0]
nums = [2, 0, 2, 1, 1, 0]
# Output: [0,0,1,1,2,2]

# bucket排序法和双指针排序法
# bucket sort


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # just 3 colors
        counts = [0, 0, 0]
        for n in nums:
            counts[n] += 1

        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1
        return nums

    def sortColors_tp(self, nums):
        left, right = 0, len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                i -= 1

            i += 1

        return nums


solution = Solution()
arr = solution.sortColors_tp(nums)
print(arr)
