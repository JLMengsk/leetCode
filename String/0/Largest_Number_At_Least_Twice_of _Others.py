# -*- coding:utf-8 -*-
# @Time     : 6/6/2020 8:17 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Largest_Number_At_Least_Twice_of +Others.py
# @Software : PyCharm

# In a given integer array nums, there is always exactly one largest element.
# Find whether the largest element in the array is at least twice as much as every other number in the array.
# If it is, return the index of the largest element, otherwise return -1.
import copy


# Can't work in leetcode
class Solution1:
    def dominantIndex(self, nums):
        a = copy.copy(nums)
        m1 = max(a)
        a.remove(m1)
        m2 = max(a)  # Second bigger
        if m1 >= 2 * m2:
            return nums.index(m1)
        return -1


# Quick way
class Solution2:
    def dominantIndex(self, nums):
        if len(nums) < 2:  # only one element is 1
            return 0
        else:
            sort = sorted(nums)
            if sort[-1] >= 2 * sort[-2]:
                return nums.index(sort[-1])
        return -1


# Scan All without python method
class Solution3:
    def dominantIndex(self, nums):
        maxIndex = 0
        for i in range(0, len(nums)):
            if (nums[i] > nums[maxIndex]):
                maxIndex = i

        for i in range(len(nums)):
            if (maxIndex != i and nums[maxIndex] < (2 * nums[i])):
                return -1
        return maxIndex


# Linear Scan
class Solution4(object):
    def dominantIndex(self, nums):
        m = max(nums)
        if all(m >= 2 * x for x in nums if x != m):
            return nums.index(m)
        return -1
        """
        all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
        元素除了是 0、空、None、False 外都算 True。
        函数等价于：
        def all(iterable):
            for element in iterable:
                if not element:
                    return False
            return True
        """


s = Solution1()
print(s.dominantIndex([1, 2, 3, 4]))
s = Solution2()
print(s.dominantIndex([1, 2, 3, 4]))
s = Solution3()
print(s.dominantIndex([1, 2, 3, 4]))
s = Solution4()
print(s.dominantIndex([1, 2, 3, 4]))
