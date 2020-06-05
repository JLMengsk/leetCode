# -*- coding:utf-8 -*-
# @Time     : 6/5/2020 2:40 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Max_Consecutive_Ones_II.py
# @Software : PyCharm

# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        zero_count = 0
        m = 0  # max length
        for i in nums:
            if i == 1:
                count += 1
            else:
                zero_count += 1
                if zero_count > 1:
                    count = 0
                    zero_count = 0
                else:
                    count += 1
            m = max(m, count)
        return m


s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]))
