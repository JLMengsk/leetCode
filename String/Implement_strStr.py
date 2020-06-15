# -*- coding:utf-8 -*-
# @Time     : 6/12/2020 12:00 AM
# @Author   : Jupiter
# @Site     : 
# @File     : Implement_strStr.py
# @Software : PyCharm

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution1:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

#Faster
class Solution2:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        return haystack.find(needle)

# 采用brute force方式，即依次从字符串的每个位置开始，截取和子字符串相同长度的字符串，与给定的子字符串进行比较。
class Solution3:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        else:
            for i in range(len(haystack) - len(needle)+1):
                # haystack: florida
                # needle:        da
                if haystack[i:i+len(needle)] == needle:
                    return i
            return -1

s = Solution1()
print(s.strStr("hello", "ll"))
s = Solution2()
print(s.strStr("hello", "ll"))
s = Solution3()
print(s.strStr("hello", "ll"))
