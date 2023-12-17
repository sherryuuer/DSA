# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Can you solve it without sorting?

# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
# Output: 4
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2,
#         3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
# k = 20
# output: 2
# nums = [3, 3, 3, 3, 4, 3, 3, 3, 3]
# k = 1
# output = 4
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 9
# output 1


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int  # index k - 1
        :rtype: int
        """
        n = len(nums)
        cur = nums[-1]

        left = 0

        for i in range(n - 1):
            if nums[i] > cur:
                tmp = nums[left]
                nums[left] = nums[i]
                nums[i] = tmp
                left += 1

        right = left

        for i in range(left, n - 1):
            if nums[i] == cur:
                tmp = nums[right]
                nums[right] = nums[i]
                nums[i] = tmp
                right += 1

        nums[-1] = nums[right]
        nums[right] = cur
        print(nums)

        if left < k <= right:
            # print(left, right)
            print(f's1:{k}:{cur}')
            return cur
        elif k <= left:
            print(f's2:{k}:{nums[:left]}')
            return self.findKthLargest(nums[:left], k)
        else:
            k = k - right - 1
            print(f's3:{k}:{nums[right + 1:]}')
            if k == 0:
                return nums[left]
            return self.findKthLargest(nums[right + 1:], k)

        # 量级思维，如果你的算法只能解决小数量级的问题，没什么用处给我点空间不行吗！
        larger = []
        smaller = []
        cur = nums.pop()
        while nums:
            if (n := nums.pop()) > cur:
                larger.append(n)
            else:
                smaller.append(n)
        if k - 1 == len(larger):
            return cur
        elif k - 1 < len(larger):
            return self.findKthLargest(larger, k)
        else:
            k = k - len(larger) - 1
            return self.findKthLargest(smaller, k)


# Solution: Sorting
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)
# 用这个不挺好的！！
class Solution1:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution2:
    def partition(self, nums: list[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill

    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]


so = Solution2()
print(so.findKthLargest(nums, k))
