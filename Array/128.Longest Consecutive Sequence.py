nums1 = [100,4,200,1,3,2]
# Output: 4
# The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


nums2 = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# deplicate 0 is not count


# steps: quick sort -> loop to get the max length
class Solution:
    def quickSort(self, nums):
        if not nums or len(nums) == 1:
            return nums

        pivot = nums[-1]
        left = 0
        for i in range(len(nums) - 1):
            if nums[i] <= pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

        nums[-1] = nums[left]
        nums[left] = pivot

        return self.quickSort(nums[: left]) + [pivot] + self.quickSort(nums[left + 1:])

    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = self.quickSort(nums)

        i = 0
        maxLength = 0

        while i < len(nums):
            curLength = 1
            while i < (len(nums) - 1) and nums[i + 1] == nums[i] + 1:
                curLength += 1
                i += 1
            maxLength = max(maxLength, curLength)
            i += 1

        return maxLength


solution = Solution()
res = solution.longestConsecutive(nums1)
print(res)


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        # Sort the array (built-in sort is O(n log n))
        nums = sorted(set(nums))  # Using set to remove duplicates

        maxLength = 1
        curLength = 1

        # Traverse the sorted unique array
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curLength += 1
            else:
                maxLength = max(maxLength, curLength)
                curLength = 1  # Reset current length for new sequence

        return max(maxLength, curLength)


# Example usage
solution = Solution()
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
res = solution.longestConsecutive(nums2)
print(res)  # Output: 9



# HashSet O(n) I think I like this one
class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # find the start point
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


# Hash Map
class Solution:
    def longestConsecutive(self, nums):
        from collections import defaultdict
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1 # mp[2] = 4
                mp[num - mp[num - 1]] = mp[num] # mp[1] = 4
                mp[num + mp[num + 1]] = mp[num] # mp[3 + 1] = 4
                res = max(res, mp[num])
        return res

nums1 = [100,4,200,1,3,2]
mp = {100: 1,
      4: 4,
      200: 1,
      1: 4,
      3: 4,
      2: 4}
res = 4
