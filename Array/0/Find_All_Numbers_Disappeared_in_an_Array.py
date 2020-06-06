# -*- coding:utf-8 -*-
# @Time     : 6/5/2020 9:09 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Find_All_Numbers_Disappeared_in_an_Array.py
# @Software : PyCharm

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.

class Solution1:
    def findDisappearedNumbers(self, nums):
        lst = []
        if len(nums) == 0:
            return None
        for i in range(1, len(nums) + 1):
            lst.append(i)
        answer = list(set(lst) - set(nums))
        return answer


class Solution2:
    def findDisappearedNumbers(self, nums):
        s = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in s]


s = Solution1()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
s = Solution2()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
