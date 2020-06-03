# -*- coding:utf-8 -*-
# @Time     : 6/3/2020 10:15 AM
# @Author   : Jupiter
# @Site     : 
# @File     : Check_IF_N_and_Its_Double_Exist.py
# @Software : PyCharm

# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

# class wrong_Solution:
#     def checkIfExist(self, arr):
#         for i in range(len(arr)):  # range(5) -----0 1 2 3 4
#             for j in range(len(arr)):
#                 if arr[i] != 0 and arr[j] != 0:  # 0 is a nut     [0,0] output should  be True
#                     if arr[i] == 2 * arr[j] or arr[i] / 2 == arr[j]:    Just need add i != j
#                         print(arr[i], arr[j])
#                         return True
#         return False

# class changed_Solution:
#     def checkIfExist(self, arr):
#         for i in range(len(arr)):
#             for j in range(len(arr)):
#                 if(arr[i] == 2 * arr[j] and i != j):
#                     return True
#
#         return False



class Solution1:
    def checkIfExist(self, arr):
        for i, a in enumerate(arr):
            for j, b in enumerate(arr):
                if i != j and a * 2 == b:
                    return True
        return False


# Hash Map
# just put what we checked in a set, and use it for next step

# for j in lst:   No need to build a list at first, check one out and put one in
# #     lst.append(i*2)

class Solution2:
    def checkIfExist(self, arr):
        checked = set()  # use a set to avoid duplicates
        for i in arr:
            if 2 * i in checked or i % 2 == 0 and i / 2 in checked:  # no () here
                # 2 situation: 1. 2*i =j  2. i/2=j
                return True
            checked.add(i)  # build hash map
        return False


s = Solution1()
print(s.checkIfExist([-2, 0, 10, -19, 4, 6, -8]))
s = Solution2()
print(s.checkIfExist([7, 1, 14, 11]))
