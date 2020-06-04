# -*- coding:utf-8 -*-
# @Time     : 6/4/2020 2:19 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Sort_Array_By_Parity.py
# @Software : PyCharm

# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# Very Good Template!!! Two-Pointer
# Noticing the outside 'j=0', recall the Bubble Sorting
# Bubble Sorting uses two iterations to get a former and a later.
class Solution1:
    def sortArrayByParity(self, A):
        j = 0
        for i in range(0, len(A)):
            if A[i] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                j += 1
        return A


# This one is slow, but same idea in other question is fast
class Solution2:
    def sortArrayByParity(self, A):
        i = count = 0
        while count < len(A):
            if A[i] % 2 == 1:
                A.append(A.pop(i))
            else:
                i += 1
            count += 1
        return A


class Solution3:
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])


class Solution4:
    def sortArrayByParity(self, A):
        return sorted(A, key=lambda x: x % 2)


s = Solution1()
print(s.sortArrayByParity([3, 1, 2, 4]))
s = Solution2()
print(s.sortArrayByParity([3, 1, 2, 4]))
s = Solution3()
print(s.sortArrayByParity([3, 1, 2, 4]))
s = Solution4()
print(s.sortArrayByParity([3, 1, 2, 4]))
