# -*- coding:utf-8 -*-
# @Time     : 6/23/2020 12:21 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Valid_Parentheses.py
# @Software : PyCharm

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# class wrong_Solution(object):
#     def isValid(self, s):
#         stack = []
#         parmap = {')': '(', '}': '{', ']': '['}
#         for i in s:
#             if i in parmap:
#                 if parmap[i] != stack.pop():  # stack = [] IndexError: pop from empty list
#                     return False
#             else:
#                 stack.append(i)
#         return len(stack) == 0


class Solution1(object):
    def isValid(self, s):
        stack = [None]
        parmap = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in parmap:
                if parmap[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        return len(stack) == 1

s = Solution1()
print(s)
