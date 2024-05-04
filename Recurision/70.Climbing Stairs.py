# https://leetcode.com/problems/climbing-stairs/description/

n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# 到定需要两步或者1步，递归问题1-1, 2-2
# M O died...
class badSolution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# solution = badSolution()
# print(solution.climbStairs(20))


# 存储dp,把算过的存进内存，不要重复了
# 自底向上的dp
class betterSolution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        solve = {}
        solve[1] = 1
        solve[2] = 2

        for i in range(3, n + 1):
            solve[i] = solve[i - 1] + solve[i - 2]
        return solve[n]


solution2 = betterSolution()
print(solution2.climbStairs(44))


# O(1)
class bestSolution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, 1
        for i in range(n - 1):
            total = left + right
            left = right
            right = total
        return right


solution3 = bestSolution()
print(solution3.climbStairs(44))
