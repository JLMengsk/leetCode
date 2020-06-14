# -*- coding:utf-8 -*-
# @Time     : 6/6/2020 2:52 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Find_Pivot_Index.py
# @Software : PyCharm

# Given an array of integers nums, write a method that returns the "pivot" index of this array.
# We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

# Very slow way
class Solution1:
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1  # When the loop is over
        # No values that meet the condition return -1


# 2a + b = sum
class Solution2:
    def pivotIndex(self, nums):
        index = -1
        sum = 0
        cur_sum = 0
        for i in range(0, len(nums)):
            sum += nums[i]
        for i in range(0, len(nums)):
            temp = sum - nums[i]
            if temp == cur_sum * 2:
                index = i
                break
            else:
                cur_sum += nums[i]
        return index


# When we refer to index and value! Think about enumerate
class Solution3:
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1


s = Solution1()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
s = Solution2()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
s = Solution3()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
