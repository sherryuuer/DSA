# Prim's算法是一种用于解决最小生成树问题的贪心算法。
# 最小生成树是一个无向连通图中的一棵包含了图中所有顶点的树，且边的权值之和最小。
# Prim's算法的基本思想是从一个初始顶点开始，每次选择一条连接已经在生成树中的顶点和不在生成树中的顶点的最小权值的边，将该边加入生成树中。
# 通过不断选择最小权值的边，最终得到最小生成树。
# 具体步骤如下：
# 1. 选择一个初始顶点作为起始点。
# 2. 将起始点加入生成树中。
# 3. 从生成树中的顶点出发，选择一条连接生成树中的顶点和不在生成树中的顶点的最小权值的边，将该边加入生成树中。
# 4. 重复步骤3，直到生成树包含了图中的所有顶点。
# Prim's算法的执行过程可以用一个优先队列（最小堆）来维护当前生成树和不在生成树中的顶点之间的最小权值边。
# 算法的时间复杂度与优先队列的实现方式有关，通常为 O(E log V)，其中 E 是边的数量，V 是顶点的数量。
# Prim's算法与Kruskal算法是解决最小生成树问题的两种主要算法，它们在不同场景下有不同的适用性。
import heapq

# Given a list of edges of a connected undirected graph,
# with nodes numbered from 1 to n,
# return a list edges making up the minimum spanning tree.


def minimumSpanningTree(edges, n):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for n1, n2, weight in edges:
        adj[n1].append([n2, weight])
        adj[n2].append([n1, weight])

    # Initialize the heap by choosing a single node
    # (in this case 1) and pushing all its neighbors.
    minHeap = []
    for neighbor, weight in adj[1]:
        heapq.heappush(minHeap, [weight, 1, neighbor])

    mst = []
    visit = set()
    visit.add(1)
    while len(visit) < n:
        weight, n1, n2 = heapq.heappop(minHeap)
        if n2 in visit:
            continue

        mst.append([n1, n2])
        visit.add(n2)
        for neighbor, weight in adj[n2]:
            if neighbor not in visit:
                heapq.heappush(minHeap, [weight, n2, neighbor])
    return mst


# 题解，求总权重，如果有不链接的node就返回-1
# 我的题解
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        import heapq
        adj = {}
        for i in range(n):
            adj[i] = []
        for n1, n2, weight in edges:
            adj[n1].append([n2, weight])
            adj[n2].append([n1, weight])

        minHeap = []
        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbor])

        total = 0
        visit = set()
        visit.add(0)
        while minHeap:
            weight, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            total += weight
            visit.add(n2)

            for neighbor, weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, n2, neighbor])

        if len(visit) < n:
            return -1
        return total


# 参考题解
class Solution:
    # Implementation for Prim's algorithm to compute Minimum Spanning Trees
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # Build the adjacency list
        adj = {}
        for i in range(n):
            adj[i] = []
        for n1, n2, weight in edges:
            adj[n1].append([n2, weight])
            adj[n2].append([n1, weight])

        minHeap = [[0, 0]]  # [vertex, weight] start bfs at v=0
        res = 0  # Total weight of the MST
        visit = set()
        while minHeap and len(visit) < n:
            weight, v = heapq.heappop(minHeap)
            if v in visit:
                continue

            res += weight
            visit.add(v)
            for neighbor, weight in adj[v]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, neighbor])

        # Return -1 if not all nodes are visited (unconnected graph)
        return res if len(visit) == n else -1
