# -*- coding:utf-8 -*-
# @Time     : 6/10/2020 9:25 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Add_Binary.py
# @Software : PyCharm

# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.

# class Solution:
#     def addBinary(self, a, b):
#         lsta = []
#         lstb = []
#         for i in a:
#             lsta.append(i)
#         for l in b:
#             lstb.append(l)
#         i ^ l
#         print(lsta)
#         print(lstb)

class Solution1:
    def addBinary(self, a, b):
        # return bin(int(a,2)+int(b,2)) #0bXXXXXX
        return bin(int(a, 2) + int(b, 2))[2:]


# class Solution2:
#     def addBinary(self, a, b):



s = Solution1()
print(s.addBinary("1010", "1101"))
s = Solution2()
print(s.addBinary("1010", "1101"))
