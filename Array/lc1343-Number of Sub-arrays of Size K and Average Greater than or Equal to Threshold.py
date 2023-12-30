# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
# Input:
arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).


class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        from collections import deque
        window = deque()
        L = 0
        res = 0
        for R in range(len(arr)):
            window.append(arr[R])
            if R - L + 1 > k:
                window.popleft()
                L += 1
            if R - L + 1 == k and sum(window) / k >= threshold:
                res += 1
        return res


solution = Solution()
res = solution.numOfSubarrays(arr, k, threshold)
print(res)
