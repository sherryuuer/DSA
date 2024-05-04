# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
numbers = [2, 7, 11, 15]
target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Your solution must use only constant extra space.
# 必须使用定量空间哦。


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L, R = 0, len(numbers) - 1
        while L < R:
            total = numbers[L] + numbers[R]
            if total == target:
                return [L + 1, R + 1]
            elif total > target:
                R -= 1
            elif total < target:
                L += 1
# 挺好的，挺典型一道题，就是输出结果反人类，干嘛不直接输出index


solution = Solution()
res = solution.twoSum(numbers, target)
print(res)
