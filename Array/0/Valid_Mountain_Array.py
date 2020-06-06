# -*- coding:utf-8 -*-
# @Time     : 6/3/2020 11:35 AM
# @Author   : Jupiter
# @Site     : 
# @File     : Valid_Mountain_Array.py
# @Software : PyCharm

# Given an array A of integers, return true if and only if it is a valid mountain array.

# class wrong_Solution:
#     def validMountainArray(self, A):
#         if len(A) < 3:
#             return False
#         maxidx = A.index(max(A))
#         for i in range(0,maxidx+1):
#             if A[i] < A[i+1]:
#                 for j in range(maxidx+1,len(A)+1):
#                 # for j in range(-1,-(len(A)-A.index(maxnum))):
#                     if j+1 < len(A):
#                         if A[j] > A[j+1]:   # out of range  Don't use ADD!
#                             return True
#             return False

# Example
# index 0 1 2 3 4 5 6 7 8 9 10
# Value 1 2 3 4 5 6 7 6 5 4 3
#                  max

class Solution1:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        maxidx = A.index(max(A))
        if (maxidx == 0) or (maxidx == len(A) - 1):   # Need to consider more situation before test
            return False
        for i in range(0, maxidx):
            if (A[i + 1] <= A[i]):
                return False
        for i in range(maxidx + 1, len(A)):
            if A[i] >= A[i - 1]:
                return False
        return True


class Solution2:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        if len(A) == 3:
            return (A[1] > A[0]) and (A[1] > A[2])
        if A[-1] > A[-2]:
            return False
        if A[0] > A[1]:
            return False

        while True:
            if A[-1] < A[-2]:
                A.pop()
            else:
                break

        while True:
            if A[-2] < A[-1]:
                A.pop()   # Use pop to save time
            else:
                break

            if len(A) == 1:
                return True
        return False


s = Solution1()
print(s.validMountainArray([0, 3, 2, 1]))
s = Solution2()
print(s.validMountainArray([0, 3, 2, 1]))
