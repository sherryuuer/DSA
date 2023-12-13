# https://leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


# 两个stack一个存储值，一个存储最小值，动态追踪最小值
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # if not self.minstack or val <= self.min:
        #     self.minstack.append(val)
        # else:
        #     self.minstack.append(self.minstack[-1])
        # simple way:
        min_val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(min_val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            del self.stack[-1]
            del self.minstack[-1]

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.stack)
param_min = obj.getMin()  # -3
print(param_min)
obj.pop()
print(obj.stack)
param_top = obj.top()  # 0
print(param_top)
param_min = obj.getMin()  # -2
print(param_min)
