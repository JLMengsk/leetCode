# -*- coding:utf-8 -*-
# @Time     : 6/12/2020 5:07 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Longest_Common_Prefix.py
# @Software : PyCharm

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


# if l >= len(strs[i]) or c != strs[i][l]:
# 这句是说指针超出了某一个元素长度，或者某一位不相等了，那么返回前面相等的即可strs[0][:l]，
# 反之就是指针没有超出任一元素长度且每一位都相等那么返回strs中第一个元素即可strs[0]
class Solution1:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        for l in range(len(strs[0])):
            c = strs[0][l]
            for i in range(len(strs)):
                if l >= len(strs[i]) or c != strs[i][l]:
                    return strs[0][:l]
        return strs[0]


# GOOD way use enumerate
class Solution2:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        pref = strs[0]
        for i, item in enumerate(strs):
            while not strs[i].find(pref) == 0:
                pref = pref[:-1]
        return pref


s = Solution1()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
s = Solution2()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
