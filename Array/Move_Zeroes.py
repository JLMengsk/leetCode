# -*- coding:utf-8 -*-
# @Time     : 6/4/2020 2:09 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Move_Zeroes.py
# @Software : PyCharm

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# The ideas is correct but I meet some problems on the nums[i] nums[j] value
# class wrong_Solution1:
#     def moveZeroes(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         j = 0
#         for i in range(0,len(nums)):
#             if nums[i] != 0:   #  NO i=j!!!! NO!
#                 nums[i], nums[j+1] = nums[j+1],nums[i]  # Set nums[i]=0
#                 j += 1
#         return nums

# class wrong_Solution2:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         j = 0
#         for i in range(0, len(nums)):
#             if nums[i] != 0 and j != i:
#                 nums[j] = nums[i]
#                 nums[i] = 0
#                 j += 1   #### if nums[i] is not equal to 0, j also need to move to next
#         return nums

# Corrected One:
# j = 0
# for i in range(0, len(nums)):
#     if nums[i] != 0:
#         if j != i:
#             nums[j] = nums[i]
#             nums[i] = 0
#         j += 1
# return nums


class Solution1:
    def moveZeroes(self, nums):
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1
            fast += 1
        return nums


# Very slow python way
class Solution2:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while 0 in nums:
            nums.remove(0)
            i += 1
        for a in range(0, i):
            nums.append(0)
        return nums


# A Very Python way
class Solution3:
    def moveZeroes(self, nums):
        nums[:] = [i for i in nums if i != 0] + nums.count(0) * [0]
        return nums


# pop then append
# pop could pop any i in nums   nums.pop(i)
class Solution4:
    def moveZeroes(self, nums):
        i = count = 0
        while count < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
            count += 1
        return nums

class Solution5:
    def moveZeroes(self, A):
        j = 0
        for i in range(0, len(A)):
            if A[i] != 0:
                A[i], A[j] = A[j], A[i]
                j += 1
        return A

s = Solution1()
print(s.moveZeroes([2, 1]))
s = Solution2()
print(s.moveZeroes([0, 1, 0, 3, 12]))
s = Solution3()
print(s.moveZeroes([0, 1, 0, 3, 12]))
s = Solution4()
print(s.moveZeroes([0, 1, 0, 3, 12]))
s = Solution5()
print(s.moveZeroes([0, 1, 0, 3, 12]))
