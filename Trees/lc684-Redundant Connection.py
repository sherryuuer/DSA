# https://leetcode.com/problems/redundant-connection/description/


class UnionFind:
    def __init__(self):
        self.par = {}
        self.rank = {}

    def find(self, n):
        # to find root of n
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

        return True


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return None
        unionfind = UnionFind()
        for edge in edges:
            for n in edge:
                if n not in unionfind.par:
                    unionfind.par[n] = n
                    unionfind.rank[n] = 0
            if not unionfind.union(edge[0], edge[1]):
                return [edge[0], edge[1]]


edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
solution = Solution()
res = solution.findRedundantConnection(edges)
print(res)


# or write like:
# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         par = [i for i in range(len(edges) + 1)]
#         rank = [1] * (len(edges) + 1)

#         def find(n):
#             p = par[n]
#             while p != par[p]:
#                 par[p] = par[par[p]]
#                 p = par[p]
#             return p

#         # return False if already unioned
#         def union(n1, n2):
#             p1, p2 = find(n1), find(n2)

#             if p1 == p2:
#                 return False
#             if rank[p1] > rank[p2]:
#                 par[p2] = p1
#                 rank[p1] += rank[p2]
#             else:
#                 par[p1] = p2
#                 rank[p2] += rank[p1]
#             return True

#         for n1, n2 in edges:
#             if not union(n1, n2):
#                 return [n1, n2]
