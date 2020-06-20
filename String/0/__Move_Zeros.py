# -*- coding:utf-8 -*-
# @Time     : 6/19/2020 9:11 PM
# @Author   : Jupiter
# @Site     : 
# @File     : __Move_Zeros.py
# @Software : PyCharm

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# class wrong_Solution:
#     def moveZeroes(self, nums):
#         for i in nums:
#             if i == 0:
#                 nums.append(nums.pop(i))
#         return nums

class Solution1:
    def moveZeroes(self, nums):
        i = 0
        for j in nums:
            if j != 0:
                nums[i] = j
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1
        return nums

s = Solution1()
print(s.moveZeroes([0,1,0,3,12]))
