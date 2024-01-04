# Find the length of the longest subarray,
# with the same value in each position.
# O(n)
def longestSubarray(nums):
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        length = max(length, R - L + 1)
    return length


def longestSubarray_2(nums):
    length = 0
    maxlength = float("-inf")
    for i in range(len(nums)):
        length += 1
        maxlength = max(length, maxlength)
        if nums[i] != nums[i - 1]:
            length = 1
    return maxlength


nums = [4, 2, 2, 3, 3, 3]
res = longestSubarray_2(nums)
print(res)


# Find the minimum length  subarray, where the sum is greater than
# or equal to the target, Assume all values are positive.
# O(n)
def shortestSubarray(nums, target):
    L, total = 0, 0
    length = float("inf")
    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1
    return 0 if length == float("inf") else length


nums = [2, 3, 1, 2, 4, 3]
target = 6
res = shortestSubarray(nums, target)
print(res)
