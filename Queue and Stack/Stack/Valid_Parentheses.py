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


class Solution2(object):
    def isValid(self, s):
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        n = 0
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
                n += 1
            else:
                if n < 1:
                    return False
                if d[stack[n - 1]] == c:
                    stack.pop()
                    n -= 1
                else:
                    return False
        if n == 0:
            return True
        else:
            return False


s = Solution1()
print(s.isValid("{[]}"))
s = Solution2()
print(s.isValid("{[]}"))
