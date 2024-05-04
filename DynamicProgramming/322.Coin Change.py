# https://leetcode.com/problems/coin-change/description/


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    # coin = 4, min(dp[4], 1 + dp[7 - 4])
        return dp[amount] if dp[amount] != float("inf") else -1

        # 超时了！！！
        # coins.sort(reverse=True)

        # def dfsHelper(i, amount, count):
        #     # Base cases
        #     if amount == 0:
        #         return count
        #     if i == len(coins):
        #         return float('inf')  # If we run out of coins, return infinity

        #     # Include the current coin
        #     include = float('inf')
        #     if amount - coins[i] >= 0:
        #         include = dfsHelper(i, amount - coins[i], count + 1)

        #     # Skip the current coin
        #     skip = dfsHelper(i + 1, amount, count)

        #     # Choose the minimum count between including and skipping the current coin
        #     return min(include, skip)

        # result = dfsHelper(0, amount, 0)

        # # If result is still infinity, it means it's not possible to make the amount
        # return result if result != float('inf') else -1


coins = [1, 2, 5]
amount = 11
solution = Solution()
res = solution.coinChange(coins, amount)
print(res)
