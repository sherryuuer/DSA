# https://leetcode.com/problems/product-of-array-except-self/description/


# 第一个解法被网友的2bcase打败了，超时
from typing import List


class Solution_v1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            total = 1
            L, R = i, i
            while L > 0:
                L -= 1
                total *= nums[L]
            while R < len(nums) - 1:
                R += 1
                total *= nums[R]
            res.append(total)
        return res


# 前缀积问题哈哈, 这个通过了居然
class Solution_v2(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        total = 1
        for n in nums:
            total *= n
            prefix.append(total)

        postfix = [None] * len(nums)
        total = 1
        index = -1
        for n in nums[::-1]:
            total *= n
            postfix[index] = total
            index -= 1

        res = [postfix[1],]
        for i in range(1, len(nums) - 1):
            res.append(prefix[i - 1] * postfix[i + 1])
        res.append(prefix[-2])

        return res


# 优化，不实用pre和post的memory，直接错位存储在output的memory中，然后在计算post的时候，直接计算出结果，天才！
class Solution_v3(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        presum = 1
        for n in nums:
            presum *= n
            output.append(presum)

        postsum = 1
        i = len(nums)
        while i > 0:
            output[i - 1] = (postsum * output[i - 2]
                             ) if i - 2 >= 0 else postsum
            postsum *= nums[i - 1]
            i -= 1

        return output


# 进一步优化
class Solution_v4(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 计算左边元素的乘积
        left_products = [1] * n
        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]

        # 计算右边元素的乘积，并将结果直接乘到左边元素的乘积上
        right_product = 1
        for i in range(n - 1, -1, -1):
            left_products[i] *= right_product
            right_product *= nums[i]

        return left_products


nums = [1, 2, 3, 4]
# Output: [24,12,8,6]
solution = Solution_v3()
res = solution.productExceptSelf(nums)
print(res)
