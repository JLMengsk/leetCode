# -*- coding:utf-8 -*-
# @Time     : 6/6/2020 8:38 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Plus_One.py
# @Software : PyCharm

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

class Solution1:
    def plusOne(self, digits):
        return list(map(int, [char for char in str(int("".join([str(s) for s in digits])) + 1)]))


# Or
# st = ''
# for item in digits:
#     st += str(item)
# st = str(int(st) + 1)
# return st

# Or
# Very important way
# results = list(map(str,digits))

# Change Array to numbers
# results="".join(results)

# results = str(int(results)+1)

# Changer numbers to array
# results = [char for char in results]

# results = list(map(int,results))
# return results

# Set flag to 1 but slow
class Solution2:
    def plusOne(self, digits):
        flag = 1
        for i in range((len(digits)) - 1, -1, -1):
            if digits[i] + flag == 10:
                digits[i] = 0
                flag = 1
            else:
                digits[i] += flag
                flag = 0

        if flag == 1:
            digits.insert(0, 1)  # list.insert(index, obj)
        return digits


s = Solution1()
print(s.plusOne([1, 2, 3]))
s = Solution2()
print(s.plusOne([1, 2, 3]))
