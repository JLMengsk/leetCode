# -*- coding:utf-8 -*-
# @Time     : 6/2/2020 5:53 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Merge_Sorted_Array.py
# @Software : PyCharm

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

class Solution:
    def merge(self, nums1,nums2):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[0:len(nums1)-len(nums2)]
        nums1 += nums2
        nums1.sort()
        return nums1

s = Solution()
print(s.merge([1,2,3,0,0,0],[2,5,6]))