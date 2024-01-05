# Union Find
# Disjoint sets
# Union-Find（并查集）是一种用于处理集合的数据结构，主要支持两个操作：
# Union（合并）和Find（查找）。
# 它用于解决一些集合合并、划分等问题，尤其是在图论和网络连接等应用中。
class UnionFind:
    def __init__(self, n):
        self.par = {}  # parent
        self.rank = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0

    # Fine parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]  # path compression
            p = self.par[p]
        return p

    # Union by height / rank
    # Return false if already connected, true otherwise
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


myuf = UnionFind(5)
print(myuf.par)
# {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
print(myuf.rank)
# {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}


# 基本思想：
# 每个元素都是一个单独的集合，最初互不相交。
# Union 操作用于合并两个集合，将它们合并成一个集合。
# Find 操作用于确定元素属于哪个集合。
# 通常，Find 操作返回集合的代表元素，可以用来检测两个元素是否属于同一个集合。

# 实现方式：
# Quick Find：
# 使用一个数组来表示集合，数组的索引表示元素，数组的值表示元素所属的集合。
# Union 操作即为修改数组中的值。Find 操作直接查找数组中的值即可。
# 但 Quick Find 的 Union 操作的时间复杂度较高，为 O(N^2)，因为每次合并都要遍历整个数组。
# Quick Union：
# 使用树状结构表示集合，每个节点都有一个父节点，树的根节点表示集合的代表元素。
# Union 操作即为将一个树的根节点连接到另一个树的根节点。Find 操作为查找元素所在树的根节点。
# Quick Union 的平均时间复杂度较好，为 O(log N)。
# Weighted Quick Union with Path Compression：
# 在 Quick Union 的基础上，通过维护每个树的大小，将小树合并到大树上，以减小树的高度。
# 同时，通过路径压缩（在 Find 操作时将路径上的节点直接连接到根节点），可以进一步减小树的高度，使 Find 操作的平均时间复杂度接近 O(1)。

# Union-Find 主要应用于图论、网络连接问题等领域，例如判断图中是否有环、Kruskal 最小生成树算法等。

class UnionFind:

    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.num_components = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        # connects x and y
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
                self.rank[py] += self.rank[px]
            else:
                self.parent[py] = px
                self.rank[px] += self.rank[py]
            self.num_components -= 1
            return True
        return False

    # def union(self, x: int, y: int) -> bool:
    #     # Connects x and y
    #     root_x = self.find(x)
    #     root_y = self.find(y)
    #     if root_x != root_y:
    #         if self.size[root_x] < self.size[root_y]:
    #             self.parent[root_x] = root_y
    #             self.size[root_y] += self.size[root_x]
    #         else:
    #             self.parent[root_y] = root_x
    #             self.size[root_x] += self.size[root_y]
    #         self.num_components -= 1
    #         return True
    #     return False

    def getNumComponents(self) -> int:
        return self.num_components
