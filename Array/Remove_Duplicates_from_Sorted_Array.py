# -*- coding:utf-8 -*-
# @Time     : 6/2/2020 8:59 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Remove_Duplicates_from_Sorted_Array.py
# @Software : PyCharm

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution1:
    def removeDuplicates(self, nums):
        nums[:] = sorted(list(set(nums)))
        return nums
        # nums = list(set(nums))
        # return len(nums)  # it can't work in leetcode


# nums[:]=sorted(list(set(nums)))  This one works

class Solution2:
    # @return an integer
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[j]:
                nums[i], nums[j + 1] = nums[j + 1], nums[i] # no matter how much is nums[i]   Just get j
                j = j + 1
        return j + 1


s = Solution1()
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
s = Solution2()
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
