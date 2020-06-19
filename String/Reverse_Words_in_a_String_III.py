# -*- coding:utf-8 -*-
# @Time     : 6/13/2020 9:06 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Reverse_Words_in_a_String_III.py
# @Software : PyCharm

# Given a string, you need to reverse the order of characters
# in each word within a sentence while still preserving whitespace and initial word order.

class Solution1:
    def reverseWords(self, s):
        return " ".join(s[::-1].split()[::-1])


class Solution2:
    def reverseWords(self, s):
        s_list = s.split()
        s_reverse = ''
        for i, word in enumerate(s_list):
            r_word = word[::-1]
            s_reverse += r_word
            if i < len(s_list) - 1:
                s_reverse += ' '   # add space
        return s_reverse


s = Solution1()
print(s.reverseWords("Let's take LeetCode contest"))
s = Solution2()
print(s.reverseWords("Let's take LeetCode contest"))
