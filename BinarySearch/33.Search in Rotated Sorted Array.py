# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0
# output: 4

# constraints:
# [] return -1 / not in the array, return -1
# O(logn) -> binary search
# steps:
# valiables: L, R
# 1, M = (L + R)//2
# 2, compare target with Middle value, between them re range
# 3, return the index


def binarySearch(nums, target):
    L, R = 0, len(nums) - 1
    while L <= R:
        M = (L + R) // 2
        if target == nums[M]:
            return M

        if nums[L] <= nums[M]:
            if target >= nums[L] and target <= nums[M]:
                R = M - 1
            else:
                L = M + 1
        else:
            if target >= nums[M] and target <= nums[R]:
                L = M + 1
            else:
                R = M - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 6

print(binarySearch(nums, target))


# nums = [4, 5, 6, 7, 0, 1, 2]
# nums = [6, 7, 0, 1, 2, 3, 4]
# target = 1

# L, R = 5, 5
# M = 4
