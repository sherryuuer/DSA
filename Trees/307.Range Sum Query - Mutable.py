# https://leetcode.com/problems/range-sum-query-mutable/description/

class Node:
    def __init__(self, total, left, right):
        self.sum = total
        self.leftroot = None
        self.righroot = None
        self.left = left
        self.right = right


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        def build(nums, left, right):
            if left == right:
                return Node(nums[left], left, right)
            mid = (left + right) // 2
            root = Node(0, left, right)
            root.leftroot = build(nums, left, mid)
            root.rightroot = build(nums, mid + 1, right)
            root.sum = root.leftroot.sum + root.rightroot.sum
            return root

        self.root = build(nums, 0, len(nums)-1)

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        def _update(root, index, val):
            if root.left == root.right:
                root.sum = val
                return

            mid = (root.left + root.right) // 2
            if index > mid:
                _update(root.rightroot, index, val)
            else:
                _update(root.leftroot, index, val)
            root.sum = root.leftroot.sum + root.rightroot.sum
        return _update(self.root, index, val)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def _sumRange(root, left, right):
            if left == root.left and right == root.right:
                return root.sum
            mid = (root.left + root.right) // 2
            if left > mid:
                return _sumRange(root.rightroot, left, right)
            elif right <= mid:
                return _sumRange(root.leftroot, left, right)
            else:
                return _sumRange(root.leftroot, left, mid) + _sumRange(root.rightroot, mid + 1, right)

        return _sumRange(self.root, left, right)


# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]


# from leetcode solutions
class NumArray:
    nums = []
    s = 0
    l = 0

    def __init__(self, nums):
        self.nums = nums
        self.s = sum(nums)
        self.l = len(nums)

    def update(self, index: int, val: int):
        self.s -= self.nums[index]
        self.nums[index] = val
        self.s += self.nums[index]

    def sumRange(self, left: int, right: int):
        if right - left > self.l // 2:
            ans = sum(self.nums[:left]) + sum(self.nums[right + 1:])
            return self.s - ans
        else:
            return sum(self.nums[left: right + 1])
