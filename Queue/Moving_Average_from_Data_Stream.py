# -*- coding:utf-8 -*-
# @Time     : 6/21/2020 5:17 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Moving_Average_from_Data_Stream.py
# @Software : PyCharm

# Given a stream of integers and a window size, calculate the moving average of all integers
# in the sliding window.

import collections


class MovingAverage:
    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.data = collections.deque(maxlen=size)

    def next(self, val):
        self.data.append(val)
        return sum(self.data) / len(self.data)


m = MovingAverage(3)
print(m.next(1))
print(m.next(10))
print(m.next(3))
print(m.next(5))