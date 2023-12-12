# https://leetcode.com/problems/contains-duplicate/

# 有重的数字的话就是true
# Example 2:
nums = [1, 2, 3, 4]
# Output: false
# Example 3:
nums2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true


class mySolution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hasht = {}
        for n in nums:
            if n in hasht:
                return True
            else:
                hasht[n] = 1
        return False

    def containsDuplicate2(self, nums):
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


s = Solution()
r = s.containsDuplicate(nums2)
print(r)
