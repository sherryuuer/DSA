# https://leetcode.com/problems/ipo/description/
# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
import heapq


class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1 * p)
            if not maxProfit:
                break
            w += -1 * heapq.heappop(maxProfit)
        return w
