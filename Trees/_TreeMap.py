# in python
# from sortedcontainers import SortedDict
# treemap = SortedDict({'c': 3, 'a': 1, 'b': 2})


class TreeNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:

    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return

        cur = self.root
        while True:
            if key < cur.key:
                if cur.left == None:
                    cur.left = newNode
                    return
                cur = cur.left
            elif key > cur.key:
                if cur.right == None:
                    cur.right = newNode
                    return
                cur = cur.right
            else:
                cur.val = val
                return

    def get(self, key: int) -> int:
        if not self.root:
            return -1

        cur = self.root
        while cur:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1

    # def getminnode(self, cur: TreeNode):
    #     cur = self.root
    #     while cur and cur.left:
    #         cur = cur.left
    #     return cur

    def getMin(self) -> int:
        if not self.root:
            return -1

        cur = self.root
        while cur and cur.left:
            cur = cur.left
        return cur.val

    def getMax(self) -> int:
        if not self.root:
            return -1

        cur = self.root
        while cur and cur.right:
            cur = cur.right
        return cur.val

    def remove(self, key: int) -> None:

        def getminnode(cur: TreeNode):
            cur = self.root
            while cur and cur.left:
                cur = cur.left
            return cur

        def helper(cur: TreeNode, key):
            if not cur:
                return None

            if key < cur.key:
                cur.left = helper(cur.left, key)
            elif key > cur.key:
                cur.right = helper(cur.right, key)
            else:
                if not cur.left:
                    return cur.right
                elif not cur.right:
                    return cur.left
                else:
                    rightmin = getminnode(cur.right)
                    cur.key = rightmin.key
                    cur.val = rightmin.val
                    cur.right = helper(cur.right, rightmin.key)
            return cur

        self.root = helper(self.root, key)

    def getInorderKeys(self) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.key)
            inorder(root.right)
        inorder(self.root)

        return res
