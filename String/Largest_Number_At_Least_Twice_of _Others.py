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
        m2 = max(a)
        if m1 >= 2 * m2:
            return nums.index(m1)
        return -1


class Solution2:
    def dominantIndex(self, nums):
        if len(nums) < 2:
            return 0
        else:
            sort = sorted(nums)
            if sort[-1] >= 2 * sort[-2]:
                return nums.index(sort[-1])
        return -1


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


s = Solution1()
print(s.dominantIndex([1, 2, 3, 4]))
s = Solution2()
print(s.dominantIndex([1, 2, 3, 4]))
s = Solution3()
print(s.dominantIndex([1, 2, 3, 4]))
