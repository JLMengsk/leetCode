# -*- coding:utf-8 -*-
# @Time     : 6/1/2020 11:42 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Max_Consecutive_Ones.py
# @Software : PyCharm

# Given a binary array, find the maximum number of consecutive 1s in this array
class Solution1:
    def findMaxConsecutiveOnes(self, nums):
        """
           :type nums: List[int]
           :rtype: int
        """
        # a = 1  In this question, there are just 1s and 0s
        max = 0
        count = 0
        for i in range(0, len(nums)):  # RANGE(0,6) ---- 0 1 2 3 4 5
            # if a == nums[i]:  # This a is useless
            if nums[i] == 1:
                count += 1
                max = max if max > count else count # COOL METHOD
                # if count > max:
                #     max = count  # need to compare with the max number
            else:
                count = 0
        return max  # find the maximum number of consecutive 1s in this array


s = Solution1()  # Instantiated
print(s.findMaxConsecutiveOnes([0, 1, 1, 1, 0, 1, 1]))


class Solution2:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(max("".join(map(str, nums)).split("0")))