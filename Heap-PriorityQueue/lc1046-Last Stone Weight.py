# https://leetcode.com/problems/last-stone-weight/description/
import heapq
stones = [2, 7, 4, 1, 8, 1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones = sorted(stones)
            m = stones.pop()
            n = stones.pop()
            if abs(m - n) != 0:
                stones.append(abs(m - n))
        return stones[0] if stones else 0


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

# There's a private _heapify_max method.
# https://github.com/python/cpython/blob/1170d5a292b46f754cd29c245a040f1602f70301/Lib/heapq.py#L198


class Solution(object):
    def lastStoneWeight(self, stones):
        heapq._heapify_max(stones)
        while len(stones) > 1:
            max_stone = heapq._heappop_max(stones)
            diff = max_stone - stones[0]
            if diff:
                heapq._heapreplace_max(stones, diff)
            else:
                heapq._heappop_max(stones)

        stones.append(0)
        return stones[0]


s = Solution()
print(s.lastStoneWeight(stones))
