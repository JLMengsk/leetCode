# -*- coding:utf-8 -*-
# @Time     : 6/23/2020 8:19 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Daily_Temperatures.py
# @Software : PyCharm

# Given a list of daily temperatures T, return a list such that,
# for each day in the input, tells you how many days you would have to wait until a warmer temperature.
# If there is no future day for which this is possible, put 0 instead.

# class wrong_Solution:
#     def dailyTemperatures(self, T):
#         stack = [101]
#         days = []
#         n = 0
#         for i in T:
#             if i > stack[-1]:
#                 n += 1
#                 days.append(n)
#                 n = 0
#                 stack.append(i)
#             else:
#                 stack.append(i)

class Solution1:
    def dailyTemperatures(self, T):
        s = []
        res = [0 for _ in range(len(T))]
        for i in range(len(T)):
            while len(s) != 0 and T[i] > T[s[-1]]:
                res[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)
        return res


s = Solution1()
print(s)
