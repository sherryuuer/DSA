# https://leetcode.com/problems/concatenation-of-array/
# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:

nums = [1, 3, 2, 1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

# double the arr?


class mySolution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            nums.append(nums[i])
        return nums

    def getConcatenation2(self, nums):
        return nums + nums

    def getConcatenation3(self, nums):
        arr = []
        for i in range(2):
            for n in nums:
                arr.append(n)

        return arr


mysolu = mySolution()
result = mysolu.getConcatenation3(nums)
print(result)
