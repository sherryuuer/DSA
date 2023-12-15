# https://leetcode.com/problems/sort-an-array/description/

nums = [5, 2, 3, 1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# must be O(nlogn)!!


class Solution(object):
    # insertion is not ok
    def sortArray_insertion(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            j = i - 1
            while j >= 0 and nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j -= 1
        return nums

    def sortArray_merge(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # merge conquer
        def merge(left, right):
            res = []
            leftidx = 0
            rightidx = 0
            while leftidx < len(left) and rightidx < len(right):
                if left[leftidx] <= right[rightidx]:
                    res.append(left[leftidx])
                    leftidx += 1
                else:
                    res.append(right[rightidx])
                    rightidx += 1

            return res + left[leftidx:] + right[rightidx:]

        # mergesort divide
        if len(nums) == 1:
            return nums

        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]

        return merge(self.sortArray_merge(left), self.sortArray_merge(right))


soso = Solution()
res = soso.sortArray_merge(nums)
print(res)
