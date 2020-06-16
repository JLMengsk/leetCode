# -*- coding:utf-8 -*-
# @Time     : 6/13/2020 12:08 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Array_Partition_I.py
# @Software : PyCharm

# Given an array of 2n integers, your task is to group these integers into n pairs of integer,
# say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

class Solution1:
    def arrayPairSum(self, nums):
        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum

# equal to: return sum(sorted(nums)[::2])    more python


s = Solution1()
print(s.arrayPairSum([1,4,3,2]))
# s = Solution2()
# print(s)
# s = Solution3()
# print(s)
