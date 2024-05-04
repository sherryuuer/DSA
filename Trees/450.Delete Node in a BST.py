# https://leetcode.com/problems/delete-node-in-a-bst/description/
root = [5, 3, 6, 2, 4, None, 7]
key = 3
# Output: [5,4,6,2,null,null,7]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def findsmallest(root):
            cur = root
            while cur and cur.left:
                cur = cur.left
            return cur

        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minnode = findsmallest(root.right)
                root.val = minnode.val
                root.right = self.deleteNode(root.right, minnode.val)

        return root

        # iter find node
        current = root
        while cur and cur.left:
            if cur.val == key:
                break
            cur = cur.left
