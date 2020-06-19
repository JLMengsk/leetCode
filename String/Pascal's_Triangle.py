# -*- coding:utf-8 -*-
# @Time     : 6/19/2020 1:58 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Pascal's_Triangle.py
# @Software : PyCharm

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

class Solution1:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle


s = Solution1()
print(s.generate(5))
