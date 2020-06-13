# -*- coding:utf-8 -*-
# @Time     : 6/13/2020 5:38 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Minimum_Size_Subarray_Sum.py
# @Software : PyCharm

# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

class Solution1:
    def minSubArrayLen(self, s, nums):
        nums.sort()
        sum = 0
        lst = []
        for i in range(len(nums)-1,-1,-1):
            if sum >= s:
                break
            else:
                sum += nums[i]
                lst.append(nums[i])
        return len(lst)


class Solution2:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """



s = Solution1()
print(s.minSubArrayLen(213,
[12,28,83,4,25,26,25,2,25,25,25,12]))
s = Solution1()
print(s.minSubArrayLen(213,
[12,28,83,4,25,26,25,2,25,25,25,12]))
