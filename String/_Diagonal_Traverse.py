# -*- coding:utf-8 -*-
# @Time     : 6/8/2020 2:10 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Diagonal_Traverse.py
# @Software : PyCharm

# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]


# I am stuck by this question...
# 右上方移动的边界条件：上边界到顶x=0，右边界到头y=n
# 左下方移动的边界条件：下边界到底x=m，左边界到投y=0
# class Solution1:
#     def findDiagonalOrder(self, matrix):
#         if matrix == []:
#             return []
#         ans = []
#         row, col = len(matrix), len(matrix[0])
#         if row == 1:
#             return matrix[0]
#         for num in range(row + col):
#             if num % 2 == 0:
#                 for i in range(num + 1):
#                     if i >= col:
#                         break
#                     if num - i >= row:
#                         continue
#                     ans.append(matrix[num - i][i])
#             else:
#                 for i in range(num + 1):
#                     if i >= row:
#                         break
#                     if num - i >= col:
#                         continue
#                     ans.append(matrix[i][num - i])
#         return ans






s = Solution1()
print(s.findDiagonalOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
s = Solution2()
print(s.findDiagonalOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
