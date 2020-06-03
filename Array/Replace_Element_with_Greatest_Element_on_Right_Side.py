# -*- coding:utf-8 -*-
# @Time     : 6/3/2020 7:49 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Replace_Element_with_Greatest_Element_on_Right_Side.py
# @Software : PyCharm

# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.#

# in-place but this one costs time
class Solution1:
    def replaceElements(self, arr):
        for i in range(0, len(arr) - 1):
            arr[i] = max(arr[i + 1:])
        arr[-1] = -1
        return arr


# Use temp to compare each other
# for i in range(len([1,2,3,4,5,6])-1,-1,-1):
#     print(i) -----5 4 3 2 1 0
class Solution2:
    def replaceElements(self, arr):
        right = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]  # swap
            arr[i] = right
            right = max(right, temp)
        return arr


s = Solution1()
print(s.replaceElements([17, 18, 5, 4, 6, 1]))
s = Solution2()
print(s.replaceElements([17, 18, 5, 4, 6, 1]))
