# -*- coding:utf-8 -*-
# @Time     : 6/12/2020 8:43 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Reverse_String.py
# @Software : PyCharm

# Write a function that reverses a string. The input string is given as an array of characters char[].

class Solution1:
    def reverseString(self, s):
        return s[::-1]

class Solution2:
    def reverseString(self, s):
        i = 0
        j= len(s)-1
        # if i != j and  i != (len(s)-1)/2:
        # if i != j:
        while i < j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -=1


class Solution3:
    def reverseString(self, s):
        lst = []
        for i in range(len(s)):
            lst.append(s.pop())
        return lst

# class Solution2:
#     def reverseString(self, s):

s = Solution1()
print(s.reverseString(["h", "e", "l", "l", "o"]))
s = Solution2()
print(s.reverseString(["h", "e", "l", "l", "o"]))
s = Solution3()
print(s.reverseString(["h", "e", "l", "l", "o"]))
