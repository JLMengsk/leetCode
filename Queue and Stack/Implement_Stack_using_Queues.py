# -*- coding:utf-8 -*-
# @Time     : 6/28/2020 4:44 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Implement_Stack_using_Queues.py
# @Software : PyCharm

class MyStack1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)

    def top(self):
        """
        Get the top element.
        """
        return self.queue[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return not self.queue

# # Run time out
# class MyStack2:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.queue1 = []
#         self.queue2 = []
#         self.top = None
#
#     def push(self, x):
#         """
#         Push element x onto stack.
#         """
#         self.queue1.insert(0, x)
#         self.top = x
#
#     def pop(self):
#         """
#         Removes the element on top of the stack and returns that element.
#         """
#         while len(self.queue1) > 1:
#             self.top = self.queue1.pop()
#             self.queue2.insert(0,self.top)
#         self.queue1.pop()
#         self.queue1, self.queue2 = self.queue2, self.queue1
#
#     def top(self) -> int:
#         """
#         Get the top element.
#         """
#         return self.top
#
#     def empty(self) -> bool:
#         """
#         Returns whether the stack is empty.
#         """
#         return not self.queue1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
