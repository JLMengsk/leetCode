# -*- coding:utf-8 -*-
# @Time     : 6/2/2020 10:22 AM
# @Author   : Jupiter
# @Site     : 
# @File     : Find_Numbers_with_Even_Number_of_Digits.py
# @Software : PyCharm

# Given an array nums of integers, return how many of them contain an even number of digits.

# class  wrong_Solution:
#     def findNumbers(self, nums):
#         # a = 100  No need to set a number to represent quotient
#         count = 0
#         digits = 0 Digits is not a variable here
#         for i in range(0,len(nums)):  we could get num directly
#             # while 10 <= a:      it's ok, but need to set initial digits to 1
#             while nums[i] > 0:
#                 # a = nums[i] // 10
#                 nums[i] //= 10
#                 digits += 1
#             if digits[i] // 2 == 0:  It is floor division, 100 // 2 = 50    37 // 2 = 18
#                 count += 1
#         return count

class Solution1:
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            digits = 0
            while num >= 1:
                num /= 10
                digits += 1
            if digits % 2 == 0:  # It is remainder
                count += 1
        return count


# This is a very smart way to transfer number to str
# So we could calculate the length
# Try to use a concise way
class Solution2:
    def findNumbers(self, nums):
        return len([i for i in nums if len(str(i)) % 2 == 0])


s = Solution1()
print(s.findNumbers([555, 901, 482, 1771]))
s = Solution2()
print(s.findNumbers([555, 901, 482, 1771]))
