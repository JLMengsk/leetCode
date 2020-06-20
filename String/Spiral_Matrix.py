# -*- coding:utf-8 -*-
# @Time     : 6/8/2020 6:40 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Spiral_Matrix.py
# @Software : PyCharm

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

# How to print a spiral matrix
# import numpy as np
#
# class Solution:
#     def spiralOrder(self, matrix):
#         x = len(matrix)
#         y = len(matrix[0])
#         myArray = np.zeros((x, y), dtype=np.int16)
#         i, j, num = 0, 0, 1
#         myArray[i][j] = 1
#         while (num < x * y):
#             while (j + 1 < y and myArray[i][j + 1] == 0):
#                 j += 1
#                 num += 1
#                 myArray[i][j] = num
#             while (i + 1 < x and myArray[i + 1][j] == 0):
#                 i += 1
#                 num += 1
#                 myArray[i][j] = num
#             while (j - 1 >= 0 and myArray[i][j - 1] == 0):
#                 j -= 1
#                 num += 1
#                 myArray[i][j] = num
#             while (i - 1 >= 0 and myArray[i - 1][j] == 0):
#                 i -= 1
#                 num += 1
#                 myArray[i][j] = num
#         print(myArray)

# class wrong_Solution:
#     def spiralOrder(self, matrix):
#         x = len(matrix)
#         y = len(matrix[0])
#         myArray = [0] * x * y
#         k, i, j, num = 0, 0, 0, 1
#         while (k < x * y):
#             while (j + 1 < y and myArray[k] == 0):
#                 myArray[k] = matrix[i][j]
#                 k += 1
#                 j += 1
#                 num += 1
#             while (i + 1 < x and myArray[k] == 0):
#                 myArray[k] = matrix[i][j]
#                 k += 1
#                 i += 1
#                 num += 1
#             while (j - 1 >= 0 and myArray[k] == 0):
#                 myArray[k] = matrix[i][j]
#                 k += 1
#                 j -= 1
#                 num += 1
#             while (i - 1 >= 0 and myArray[k] == 0):
#                 myArray[k] = matrix[i][j]
#                 k += 1
#                 i -= 1
#                 num += 1
#         print(myArray)


# Set four model for move
# 0: go right 1: go down 2: go left 3. go up

s = Solution()
print(s.spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]))
