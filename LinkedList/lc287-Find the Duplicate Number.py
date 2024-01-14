# https://leetcode.com/problems/find-the-duplicate-number/description/
# 因为一定会有结果所以一定是循环，所以可以条件设为while True


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums) - 1
        # slow = fast = 0
        # while fast <= n:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if fast == slow:
        #         break
        # slow2 = 0
        # while slow2 != slow:
        #     slow2 = nums[slow2]
        #     slow = nums[slow]
        # return slow

        # 更简单的版本，设为True得到结果
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow


nums = [1, 3, 4, 2, 2]
# 0 - 1
# 1 - 3
# 2 - 4
# 3 - 2
# 4 - 2
# 0 - 1 - 3 - 2 - 4 - 2

# Output: 2
solution = Solution()
res = solution.findDuplicate(nums)
print(res)
