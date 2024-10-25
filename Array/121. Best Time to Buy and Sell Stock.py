# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
prices = [7, 1, 5, 3, 6, 4]
# Output: 5 = 6 - 1
# if can' t achive, return 0
prices = [7, 6, 4, 3, 1]
# Output: 0
# can not achive


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP = 0

        L, R = 0, 1
        while R < len(prices):
            if prices[L] < prices[R]:
                curP = prices[R] - prices[L]
                maxP = max(maxP, curP)
            else:
                L = R
            R += 1
        return maxP
