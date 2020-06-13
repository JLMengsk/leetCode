# -*- coding:utf-8 -*-
# @Time     : 6/13/2020 8:10 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Rotate_Array.py
# @Software : PyCharm

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# class wrong_Solution:
#     def rotate(self, nums, k):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         return nums.append(nums.pop)

class Solution1:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = k % len(nums) # k may bigger than len(nums)
        nums[:] = nums[-i:] + nums[:-i]
        return nums

s = Solution1()
print(s.rotate([-1,-100,3,99],2))
