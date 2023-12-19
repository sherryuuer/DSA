# https://leetcode.com/problems/path-sum/description/
# Given the root of a binary tree and an integer targetSum
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def bfs(root, leafsum):
            if not root:
                return False
            leafsum += root.val

            if not root.left and not root.right:
                return leafsum == targetSum

            if bfs(root.left, leafsum):
                return True
            if bfs(root.right, leafsum):
                return True

        return bfs(root, 0)


# dp way
class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        de = [
            (root, sum - root.val),
        ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False
