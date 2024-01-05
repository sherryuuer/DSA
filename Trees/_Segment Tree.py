# llm
"""
class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        self.build(nums)

    def build(self, nums):
        for i in range(self.n, 2 * self.n):
            self.tree[i] = nums[i - self.n]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 0:
            left, right = index, index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index //= 2

    def query(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return result


# 示例用法
nums = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(nums)
print(seg_tree.tree)
print(seg_tree.query(1, 3))  # 输出：15
seg_tree.update(2, 6)
print(seg_tree.query(1, 3))  # 输出：16
"""


class SegmentTree:

    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

    # O(n)
    @staticmethod
    def build(nums, L, R):
        if L == R:
            return SegmentTree(nums[L], L, R)
        M = (L + R) // 2
        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return

        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.sum = self.left.sum + self.right.sum

    # O(logn)
    def rangeQuery(self, L, R):
        if self.L == L and self.R == R:
            return self.sum

        M = (self.L + self.R) // 2
        if L > M:
            return self.right.rangeQuery(self, L, R)
        elif R <= M:
            return self.left.rangeQuery(self, L, R)
        else:
            return (self.left.rangeQuery(self, L, M) + self.right.rangeQuery(self, M + 1, R))


# Practise
class Node:

    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R


class SegmentTree:

    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, L, R):
        if L == R:
            return Node(nums[L], L, R)

        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root, index, val):
        if root.L == root.R:
            root.sum = val
            return

        M = (root.L + root.R) // 2
        if index > M:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)
        root.sum = root.left.sum + root.right.sum

    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    def query_helper(self, root, L, R):
        if L <= root.L and root.R <= R:
            return root.sum

        if R < root.L or L > root.R:
            return 0

        return self.query_helper(root.left, L, R) + self.query_helper(root.right, L, R)
