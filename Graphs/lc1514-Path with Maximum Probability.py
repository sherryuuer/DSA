# https://leetcode.com/problems/path-with-maximum-probability/description/


# 最大概率问题？！
# 无向图，需要添加两次边
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        import heapq
        adj = {}
        for i in range(n):
            adj[i] = []

        for i, [s, d] in enumerate(edges):
            adj[s].append((d, succProb[i]))
            adj[d].append((s, succProb[i]))

        maxprobs = set()
        maxheap = [[-1 * 1, start_node]]
        while maxheap:
            w1, n1 = heapq.heappop(maxheap)
            maxprobs.add(n1)

            if n1 == end_node:
                return w1 * -1

            for n2, w2 in adj[n1]:
                if n2 not in maxprobs:
                    heapq.heappush(maxheap, [w1 * w2, n2])

        return 0


n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2
# Output: 0.25000
solution = Solution()
res = solution.maxProbability(n, edges, succProb, start, end)
print(res)


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        pq = [(-1, start)]
        visit = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visit.add(cur)

            if cur == end:
                return prob * -1
            for nei, edgeProb in adj[cur]:
                if nei not in visit:
                    heapq.heappush(pq, (prob * edgeProb, nei))
        return 0
