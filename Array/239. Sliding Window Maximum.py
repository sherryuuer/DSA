# https://leetcode.com/problems/sliding-window-maximum/description/

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]  # 选择中间元素作为基准值
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quick_sort(left) + middle + quick_sort(right)

        # 获取数组最大值
        def get_max(arr):
            sorted_arr = quick_sort(arr)
            return sorted_arr[-1] if sorted_arr else None

        left, right = 0, k
        res = []

        while right <= len(nums):
            res.append(get_max(nums[left:right]))
            left += 1
            right += 1

        return res


# 优化：单调递减队列（monotonically decreasing queue）
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        output = []
        q = deque()  # from max to min
        left = right = 0

        while right < len(nums):
            # pop smaller value from queue
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # remove left value if it is out of bounds
            if q[0] < left:
                q.popleft()

            # detect the right is increased to the window size k
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1

            right += 1

        return output
