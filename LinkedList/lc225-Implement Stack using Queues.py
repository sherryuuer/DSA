# https://leetcode.com/problems/implement-stack-using-queues/description/
# deque is very easy.
# 用queue实现stack那么只能用queue的超能力不能用pop作弊啦
from collections import deque


class MyStack(object):

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        use only a queue's standard operations.
        """
        for i in range(len(self.stack) - 1):
            self.push(self.stack.popleft())
        return self.stack.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
