# -*- coding:utf-8 -*-
# @Time     : 6/4/2020 2:22 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Height_Checker.py
# @Software : PyCharm
# Students are asked to stand in non-decreasing order of heights for an annual photo.
# Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

class Solution1:
    def heightChecker(self, heights):
        lst = sorted(heights)
        count = 0
        for i in range(len(lst)):
            if lst[i] != heights[i]:  # Compare values which have same index
                count += 1
        return count


# ZIP way
# a = [1,2,3]
# b = [4,5,6]
# zipped = zip(a,b)
# ---> [(1, 4), (2, 5), (3, 6)]
class Solution2:
    def heightChecker(self, heights):
        return sum(a != b for a, b in zip(sorted(heights), heights))


s = Solution1()
print(s.heightChecker([1, 1, 4, 2, 1, 3]))
s = Solution2()
print(s.heightChecker([1, 1, 4, 2, 1, 3]))
