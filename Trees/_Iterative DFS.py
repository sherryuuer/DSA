# Iterative DFS（迭代深度优先搜索）是深度优先搜索算法的一种实现方式，它使用栈（Stack）来模拟递归的过程。
# 与递归深度优先搜索相比，迭代深度优先搜索更容易在一些编程语言中进行优化，因为它不依赖于系统栈的调用。
# 深度优先搜索（DFS）是一种用于遍历或搜索树或图的算法，它从起始点开始，沿着一条路径尽可能深地访问，直到到达末端，然后回溯到前一步。
# DFS 通常使用递归或显式栈来实现。
class TreeNode:

    def __init(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# Time and Space O(n)
def inorder(root):
    stack = []
    curr = root

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right


# Time and Space O(n)
def preorder(root):
    stack = []
    curr = root

    while curr or stack:
        if curr:
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()


# Time and Space O(n)
def postorder(root):
    stack = [root]
    visit = [False]

    while stack:
        curr, visit = stack.pop(), visit.pop()
        if curr:
            if visit:
                print(curr.val)
            else:
                stack.append(curr)
                visit.append(True)
                stack.append(curr.right)
                visit.append(False)
                stack.append(curr.left)
                visit.append(False)
