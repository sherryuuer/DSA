# Given a directed acyclical graph, return a valid
# topological ordering of the graph.
# 上课问题，前置课程问题
def topologicalSort(edges, n):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for src, dst in edges:
        adj[src].append(dst)

    topSort = []
    visit = set()
    for i in range(1, n + 1):
        dfs(i, adj, visit, topSort)
    topSort.reverse()
    return topSort


def dfs(src, adj, visit, topSort):
    if src in visit:
        return
    visit.add(src)

    for neighbor in adj[src]:
        dfs(neighbor, adj, visit, topSort)
    topSort.append(src)
