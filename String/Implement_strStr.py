# -*- coding:utf-8 -*-
# @Time     : 6/12/2020 12:00 AM
# @Author   : Jupiter
# @Site     : 
# @File     : Implement_strStr.py
# @Software : PyCharm

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


s = Solution()
print(s.strStr("hello", "ll"))
