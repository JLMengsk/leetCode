# -*- coding:utf-8 -*-
# @Time     : 6/19/2020 9:09 PM
# @Author   : Jupiter
# @Site     : 
# @File     : __Remove_Duplicates_from_Sorted_Array.py
# @Software : PyCharm

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution1:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        cur = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cur]:
                cur += 1
                nums[cur] = nums[i]
        return cur + 1


s = Solution1()
print(s.removeDuplicates([1, 1, 2]))
