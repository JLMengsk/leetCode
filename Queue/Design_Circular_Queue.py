# -*- coding:utf-8 -*-
# @Time     : 6/20/2020 8:30 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Design_Circular_Queue.py
# @Software : PyCharm


# Design your implementation of the circular queue. The circular queue
# is a linear data structure in which the operations are performed based
# on FIFO (First In First Out) principle and the last position
# is connected back to the first position to make a circle. It is also called "Ring Buffer".
# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
# In a normal queue, once the queue becomes full, we cannot insert the next element even
# if there is a space in front of the queue. But using the circular queue,
# we can use the space to store new values.
#
# Your implementation should support following operations:
# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.

class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = []
        self.size = k
        # self.front = 0
        # self.rear = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # if self.rear - self.front < self.size:
        #     self.queue.append(value)
        #     self.rear += 1
        if not self.isFull():
            self.queue.append(value)
            return True
        else:
            return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        # if self.rear - self.front > 0:
        # self.front += 1
        if not self.isEmpty():
            self.queue.pop(0)
            return True
        else:
            return False

    def Front(self):
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[0]

    def Rear(self):
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[-1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        return 0 == len(self.queue)

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.queue) == self.size


circularQueue = MyCircularQueue(3)
print(circularQueue.enQueue(1))
print(circularQueue.enQueue(2))
print(circularQueue.enQueue(3))
print(circularQueue.enQueue(4))
print(circularQueue.Rear())
print(circularQueue.isFull())
print(circularQueue.deQueue())
print(circularQueue.enQueue(4))
print(circularQueue.Rear())


# Better way
"""
class MyCircularQueue:

    def __init__(self, k):
        self.queue = [-1] * k
        self.first = 0
        self.len = 0
        
    def enQueue(self, value):
        if self.len == len(self.queue):
            return False
        
        self.queue[(self.first+self.len)%len(self.queue)] = value
        self.len += 1
        return True

    def deQueue(self):
        if self.len == 0:
            return False
        
        self.first = (self.first+1)%len(self.queue)
        self.len -= 1
        return Ture

    def Front(self):
        return self.queue[self.first] if self.len > 0 else -1

    def Rear(self):
        return self.queue[(self.first+self.len-1)%len(self.queue)] if self.len > 0 else -1

    def isEmpty(self):
        return self.len == 0

    def isFull(self):
        return self.len == len(self.queue)
"""