# -*- coding:utf-8 -*-
# @Time     : 6/13/2020 8:36 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Reverse_Words_in_a_String.py
# @Software : PyCharm

# Given an input string, reverse the string word by word.
class Solution1:
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

s = Solution1()
print(s.reverseWords("the sky is blue"))
