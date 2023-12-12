# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


class mySolution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [nums[0],]
        count_ = 0
        for n in nums[1:]:
            if n != arr[-1]:
                arr.append(n)
            else:
                count_ += 1
        print(arr)

        return len(arr), arr + (['_']*count_)


answer = mySolution()
res = answer.removeDuplicates(nums)
print(res)


# 指针真的很清晰
# 左右指针方法，左记录不重复的位置，右遍历和比较
def removedu(nums):
    left = 1

    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1

    return left


res = removedu(nums)
print(res)
