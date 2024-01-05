# Given a list of distinct nums, return all the possible distinct subsets
# 每个元素，在子集中，或者不在子集中，0或者1问题
# Time O(n * 2^n), space O(n)
def subsetsWithoutDuplicates(nums):
    subsets, curset = [], []
    helper(0, nums, curset, subsets)
    return subsets


def helper(i, nums, curset, subsets):
    if i >= len(nums):
        subsets.append(curset.copy())
        return

    # include nums[i]
    curset.append(nums[i])
    helper(i + 1, nums, curset, subsets)
    curset.pop()
    # not include nums[i]
    helper(i + 1, nums, curset, subsets)

# Given a list of not necessarily distinct nums, return all the possible distinct subsets
# Time: O(n * 2^n), Space: O(n)


def subsetsWithDuplicates(nums):
    nums.sort()
    subsets, curset = [], []
    helper2(0, nums, curset, subsets)
    return subsets


def helper2(i, nums, curset, subsets):
    if i >= len(nums):
        subsets.append(curset.copy())
        return

    # include nums[i]
    curset.append(nums[i])
    helper2(i + 1, nums, curset, subsets)
    curset.pop()
    # not include nums[i]
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
    helper2(i + 1, nums, curset, subsets)
