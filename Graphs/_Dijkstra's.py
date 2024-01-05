import heapq

# Given a connected graph represented by a list of edges, where
# edge[0] = src, edge[1] = dst, and edge[2] = weight,
# find the shortest path from src to every other node in the 
# graph. There are n nodes in the graph.
# O(E * logV), O(E * logE) is also correct.
def shortestPath(edges, n, src):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []

    # s = src, d = dst, w = weight
    for s, d, w in edges:
        adj[s].append([w, d])

    shortest = {}
    minHeap = [[0, src]]
    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in shortest:
            continue
        shortest[n1] = w1

        for w2, n2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minHeap, [w1 + w2, n2])
    
    return shortest


# 考虑无解的情况返回设置最小路径-1
# 我的解答
  class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        import heapq
        adj = {}
        shortest = {}
        
        for i in range(n):
            adj[i] = []
            shortest[i] = -1

        for u, v, w in edges:
            adj[u].append([w, v])

        minHeap = [[0, src]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if shortest[n1] != -1:
                continue
            shortest[n1] = w1

            for w2, n2 in adj[n1]:
                if shortest[n2] == -1:
                    heapq.heappush(minHeap, [w1 + w2, n2])

        return shortest


# 示例解答
class Solution:
    # Implementation for Dijkstra's shortest path algorithm
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
            
        # s = src, d = dst, w = weight
        for s, d, w in edges:
            adj[s].append([d, w])

        # Compute shortest paths
        shortest = {}
        minHeap = [[0, src]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        
        # Fill in missing nodes
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
