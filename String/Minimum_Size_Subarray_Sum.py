# -*- coding:utf-8 -*-
# @Time     : 6/13/2020 5:38 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Minimum_Size_Subarray_Sum.py
# @Software : PyCharm

# Given an array of n positive integers and a positive integer s,
# find the minimal length of a CONTIGUOUS subarray of which the sum ≥ s. If there isn't one, return 0 instead.


# 213
# [12,28,83,4,25,26,25,2,25,25,25,12]
# Output:7   wrong!!!
# Expected:8
# class wrong_Solution:
#     def minSubArrayLen(self, s, nums):
#         nums.sort()                                 # must be contiguous!!!!
#         sum = 0
#         lst = []
#         for i in range(len(nums)-1,-1,-1):
#             if sum >= s:
#                 break
#             else:
#                 sum += nums[i]
#                 lst.append(nums[i])
#         return len(lst)


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        res = float("inf")   # length bigger than nums    could set it to oo----> float('inf')
        l,r,total = 0,0,0
        while r < len(nums):
            total += nums[r]
            while total >= s:
                res = min(res,r-l+1)
                total -= nums[l]
                l += 1
            r += 1
        return res if res != float("inf") else 0
    # enumerate
    #     if sum(nums) < s:
    #         return 0
    #     res = len(nums)
    #     left, total = 0, 0
    #     for i, n in enumerate(nums):
    #         total += n
    #         while total >= s:
    #             res = min(res, i-left+1)
    #             total -= nums[left]
    #             left += 1
    #     return res

s = Solution()
print(s.minSubArrayLen(213,
[12,28,83,4,25,26,25,2,25,25,25,12]))
