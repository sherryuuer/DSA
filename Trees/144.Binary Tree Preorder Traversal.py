# https://leetcode.com/problems/binary-tree-preorder-traversal/description/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        cur = root
        while cur or stack:
            if cur:
                res.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return res
