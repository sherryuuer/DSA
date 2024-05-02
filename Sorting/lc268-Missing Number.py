# https://leetcode.com/problems/missing-number/description/

# Given an array nums containing n distinct numbers in the range [0, n]
# return the only number in the range that is missing from the array.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # for i in range(n):
        #     val = nums[i]
        #     if val < n and val != nums[val]:
        #         nums[val], nums[i] = nums[i], nums[val]
        #     else:
        #         continue
        #
        # for i in range(n):
        #     if nums[i] != i:
        #         return i

        # return n
        len_nums = len(nums)
        index = 0

        while index < len_nums:
            value = nums[index]

            if value < len_nums and value != nums[value]:
                nums[index], nums[value] = nums[value], nums[index]

            else:
                index += 1
            print(nums)
        for x in range(len_nums):
            if x != nums[x]:
                return x
        return len_nums


solution = Solution()
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# Output: 2
res = solution.missingNumber(nums)
print(res)

# 其他解法


class Solution(object):
    def missingNumber(self, nums):
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res


def missingNumber(nums):
    n = len(nums)

    # 计算数组中所有元素的和
    nums_sum = sum(nums)

    # 计算从 1 到 n 的连续整数的和
    expected_sum = (n * (n + 1)) // 2

    # 返回缺失的数字
    return expected_sum - nums_sum
