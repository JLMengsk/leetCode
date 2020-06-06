# -*- coding:utf-8 -*-
# @Time     : 6/5/2020 4:46 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Third_Maximum_Number.py
# @Software : PyCharm

# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

# Cant't work on leetcode
# class Solution1:
#     def thirdMax(self, nums):
#         count = 0
#         if len(set(nums)) < 3:
#             return max(nums)
#         while count < 2:
#             m = max(nums)
#             while m in nums:
#                 nums.remove(m)
#             count += 1
#         return max(nums)

class Solution1_plus:
    def thirdMax(self, nums):
        nums = set(nums)
        x = max(nums)
        if len(nums) > 2:
            for i in range(2):
                nums.remove(x)
                if len(nums) != 0:
                    x = max(nums)
                else:
                    break
        return x


# Set:  Eliminate Duplicates first
class Solution2:
    def thirdMax(self, nums):
        nums.sort()
        if len(set(nums)) < 3:
            return nums[-1]
        else:
            return sorted(set(nums))[-3]


s = Solution1()
print(s.thirdMax([3, 2, 3, 2, 1]))
s = Solution2()
print(s.thirdMax([3, 2, 3, 2, 1]))
