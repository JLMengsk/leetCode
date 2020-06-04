# -*- coding:utf-8 -*-
# @Time     : 6/2/2020 12:20 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Squares_of_a_Sorted_Array.py
# @Software : PyCharm

# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

class Solution1:
    def sortedSquares(self, A):
        for i in range(len(A)):
            A[i] = (A[i] ** 2)
            # A.sort() Wrong Position
        A.sort()  # Pay attention where to use sort. Finished the whole loop then sort
        return A


class Solution2:
    def sortedSquares(self, A):
        return sorted([i * i for i in A])


# sorted() and sort()

class Solution3:
    def sortedSquares(self, A):
        j = 0
        for i in range(0, len(A)):
            if (A[i]) ** 2 > (A[j] ** 2):
                if i != j:
                    A[i], A[j] = A[j]**2, A[i]
                j += 1
        return A

s = Solution1()
print(s.sortedSquares([-4, -1, 0, 3, 10]))
s = Solution2()
print(s.sortedSquares([-4, -1, 0, 3, 10]))
s = Solution3()
print(s.sortedSquares([-4, -1, 0, 3, 10]))
