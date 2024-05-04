# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
root = [4, 2, 7, 1, 3]
val = 2
# Output: [2,1,3]
root = [4, 2, 7, 1, 3]
val = 5
# Output: []


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root
