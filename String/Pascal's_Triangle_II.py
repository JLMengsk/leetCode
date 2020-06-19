# -*- coding:utf-8 -*-
# @Time     : 6/19/2020 1:59 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Pascal's_Triangle_II.py
# @Software : PyCharm

# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.

class Solution:
    def getRow(self, rowIndex):
        triangle = []

        for row_num in range(rowIndex+1):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle[rowIndex]


s = Solution()
print(s.getRow(3))

