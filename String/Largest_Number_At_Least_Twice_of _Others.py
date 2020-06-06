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


# class Solution2:
#     def dominantIndex(self, nums):
#         checked = []
#         max = nums[0]
#         for i in range(len(nums)):
#             if max != nums[i] and max >= 2 * nums[i]:
#                 return nums.index(max)
#             else:
#                 checked.append(nums[i])


s = Solution1()
print(s.dominantIndex([1, 2, 3, 4]))
s = Solution2()
print(s.dominantIndex([1, 2, 3, 4]))
