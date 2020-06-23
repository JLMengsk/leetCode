# -*- coding:utf-8 -*-
# @Time     : 6/23/2020 11:54 AM
# @Author   : Jupiter
# @Site     : 
# @File     : Min_Stack.py
# @Software : PyCharm

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Easy One but didn't consider constant time
class MinStack1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

# !!!!!!!!!!!retrieving the minimum element in constant time
class MinStack2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        if not self.minStack or self.minStack[-1] >=x:
            self.minStack.append(x)

    def pop(self):
        if self.minStack[-1] == self.stack[-1]:
            del self.minStack[-1]
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# No need to build a stack for min
class MinStack3:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x):
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    def pop(self):
        t = self.stack[-1]
        self.stack.pop()
        if self.min == t:
            self.min = self.stack[-1]
            self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

