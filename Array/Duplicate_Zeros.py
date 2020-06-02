# -*- coding:utf-8 -*-
# @Time     : 6/2/2020 4:55 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Duplicate_Zeros.py
# @Software : PyCharm

# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place, do not return anything from your function.

# class wrong_Solution:
#     def duplicateZeros(self, arr):
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         for i in range(0, len(arr)):
#             if arr[i] == 0:
#                 arr.insert(i, 0)
#         return arr


class Solution1:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        flag = 0
        lst = []
        for i in range(0, len(arr)):
            if arr[i] == 0:
                lst.append(i)
        for item in lst:
            # print(item)
            arr.insert(flag + item, 0)
            arr.pop()  # Important
            flag += 1
        return arr


class Solution2:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.pop()
                arr.insert(i + 1, 0)
                i += 2  # There is the key
            else:
                i += 1 # There is the key
        return arr


s = Solution1()
print(s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
s = Solution2()
print(s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))


class Solution3:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        len_arr = len(arr)
        lst = []
        for num in arr:
            if num == 0:
                lst.append(0)
                lst.append(0)
            else:
                lst.append(num)
            if len(lst) >= len_arr:
                arr[:] = lst[:len_arr]
                # arr=rst[:len_arr] this do not work
                # 这道题要注意的是当用第一张方法的时候，记得要直接改变arr指向的值，而不是改变它引用本身，
                # 因为leetcode判定程序还是记录着一开始的引用值，可以去了解一下leetcode的变量引用机制。
        return arr

s = Solution3()
print(s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))