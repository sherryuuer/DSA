# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
# Example 1:
# nums = [1, 1, 1, 2, 2, 3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


class mySolution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        L, R = 0, 1
        count = 0
        while R < len(nums):
            if nums[R] == nums[L]:
                if R - L > 1:
                    nums[R] = float("inf")
                    count += 1
                    R += 1
                elif R - L == 1:
                    R += 1
            else:
                L = R
                R += 1

        nums.sort()

        return R - count


# 我很不理解力扣想让我返回什么东西，答案明明对的,然后发现就算你不return数组本身，你也要在内部给他排序，满足力扣的测试要求
# 一个非常不错的解法，左指针代表有效数组，右指针负责数有多少个重复值，将有效值不断添加到左边指针上
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L, R = 0, 0
        while R < len(nums):
            count = 1
            while R + 1 < len(nums) and nums[R] == nums[R + 1]:
                count += 1
                R += 1

            for i in range(min(2, count)):
                nums[L] = nums[R]
                L += 1

            R += 1
        return L


solution = Solution()
res = solution.removeDuplicates(nums)
print(res)
