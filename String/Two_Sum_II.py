# -*- coding:utf-8 -*-
# @Time     : 6/13/2020 12:22 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Two_Sum_II.py
# @Software : PyCharm

# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.

# Very Slow
class Solution1:
    def twoSum(self, numbers, target):
        for i in numbers:
            a = target -i
            if a == i:
                return numbers.index(i) + 1,numbers.index(i) + 2
            if a in numbers:
                return numbers.index(i) + 1, numbers.index(target - i) + 1


s = Solution1()
print(s.twoSum([2, 7, 11, 15], 9))
# s = Solution2()
# print(s)
# s = Solution3()
# print(s)
