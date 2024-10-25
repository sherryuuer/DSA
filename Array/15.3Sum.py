nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1,-1,2],[-1,0,1]]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        if len(nums) < 3:
            return res
        for i, v in enumerate(nums):
            if v > 0:
                break

            # skip duplicate
            if i > 0 and v == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = v + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    # skip duplicate
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
        return res


solution = Solution()
print(solution.threeSum(nums))
