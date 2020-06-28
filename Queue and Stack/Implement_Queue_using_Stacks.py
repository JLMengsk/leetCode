# -*- coding:utf-8 -*-
# @Time     : 6/28/2020 12:18 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Implement_Queue_using_Stacks.py
# @Software : PyCharm

# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.

class MyQueue1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.swap = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        while self.stack:
            self.swap.append(self.stack.pop())
        self.swap.append(x)
        while self.swap:
            self.stack.append(self.swap.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()

    def peek(self):
        """
        Get the front element.
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return not self.stack

class MyQueue2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.outStack.pop()

    def peek(self):
        """
        Get the front element.
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return not self.inStack and not self.outStack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

s = Solution1()
print(s)
