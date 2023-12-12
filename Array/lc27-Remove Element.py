# https://leetcode.com/problems/remove-element/
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).


class mySolution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        L = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[L] = nums[r]
                L += 1
        return L


answer = mySolution()
result = answer.removeElement(nums, val)
print(result)
