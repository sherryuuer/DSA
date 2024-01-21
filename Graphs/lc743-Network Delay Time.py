# https://leetcode.com/problems/network-delay-time/description/


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        from heapq import heappop, heappush
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for u, v, w in times:
            adj[u].append((v, w))

        shortest = {}
        minheap = [[0, k]]
        while minheap:
            w1, n1 = heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in minheap:
                    heappush(minheap, [w1 + w2, n2])
        return max(shortest.values()) if len(shortest) == n else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
# Output: 2
solution = Solution()
res = solution.networkDelayTime(times, n, k)
print(res)
