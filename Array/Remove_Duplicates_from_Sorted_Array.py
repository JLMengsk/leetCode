# -*- coding:utf-8 -*-
# @Time     : 6/2/2020 8:59 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Remove_Duplicates_from_Sorted_Array.py
# @Software : PyCharm

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums):
        nums = list(set(nums))
        return len(nums)  # I don't know why it can't work in leetcode
# nums[:]=sorted(list(set(nums)))  This one works


s = Solution()
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
