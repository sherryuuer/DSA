# Check if an array is a palindrome回文
# nums = [1, 2, 7, 7, 2, 1]

# 判断是不是回文
def isPalindrome(word):
    L, R = 0, len(word) - 1
    while L < R:
        if word[L] != word[R]:
            return False
        L += 1
        R -= 1
    return True


# Given an sorted input array, return the two indices
# if two elements which sum up to the target value.
# Assume there's exactly one solution.
# two sum!!no! this is sorted!
nums = [-1, 2, 3, 4, 7, 9]
target = 7


def twoSum(nums, target):
    L, R = 0, len(nums) - 1
    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1
        elif nums[L] + nums[R] < target:
            L += 1
        else:
            return [L, R]


res = twoSum(nums, target)
print(res)
