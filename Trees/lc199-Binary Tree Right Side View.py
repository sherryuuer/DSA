# https://leetcode.com/problems/binary-tree-right-side-view/description/
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# 广度优先搜索，只返回，每一行到最后一个值


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        queue = deque()
        res = []
        level = 0
        if not root:
            return None
        queue.append(root)

        while len(queue) > 0:
            res.append(queue[-1].val)

            for i in range(len(queue)):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        return res
