class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def canReachLeaf(root):
    # base false case
    if not root or root.val == 0:
        return False
    # base true case
    if not root.left and not root.right:
        return True
    # recurisive to find left and right
    if root.left:
        return canReachLeaf(root.left)
    if root.right:
        return canReachLeaf(root.right)
    return False


def leafPath(root, path):
    # base false case
    if not root or root.val == 0:
        return False
    # push in path list
    path.append(root)
    # base true case
    if not root.left and not root.right:
        return True
    # recurisive to find true or false
    if root.left:
        return leafPath(root, path)
    if root.right:
        return leafPath(root, path)
    path.pop()
    return False


####
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def canReachLeaf(root):
    if not root or root.val == 0:
        return False

    if not root.left and not root.right:
        return True
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    return False


def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)

    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False
