class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, root) -> None:
        self.root = TreeNode()

    def search(self, root, target):
        if not root:
            return False

        if target < root.left.val:
            return self.search(root.left, target)
        elif target > root.right.val:
            return self.search(root.right, target)
        else:
            return True
