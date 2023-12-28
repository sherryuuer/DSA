# https://leetcode.com/problems/clone-graph/description/
adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


solution = Solution()
res = solution.cloneGraph(adjList)
print(res)
