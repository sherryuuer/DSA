# https://leetcode.com/problems/binary-search-tree-iterator/description/
# next相当于一个生成器，hasnext只是判断指针下一个有没有节点


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        from collections import deque
        stack = []
        cur = root
        self.inorder = deque()
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                self.inorder.appendleft(cur.val)
                cur = cur.right

    def next(self):
        """
        :rtype: int
        """
        return self.inorder.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.inorder else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
