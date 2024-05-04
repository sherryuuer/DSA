# https://leetcode.com/problems/two-sum/

# Example 1:

nums = [2, 7, 11, 15]
target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


class mySolution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hasht = {}
        for i, n in enumerate(nums):
            if n not in hasht:
                hasht[n] = i

            if target - n in hasht:
                return [hasht[target - n], i]
        return -1


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


s = mySolution()
r = s.twoSum(nums, target)
print(r)
