# -*- coding:utf-8 -*-
# @Time     : 6/20/2020 5:51 PM
# @Author   : Jupiter
# @Site     : 
# @File     : __Max_Consecutive_Ones.py
# @Software : PyCharm

class Solution1:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max = 0
        for i in nums:
            if i == 1:
                count += 1
                max = max if max > count else count
            else:
                count = 0
        return max

"""
maxCons = 0
cons = 0

for num in nums:
    if num == 1:
        cons += 1
    else:
        if cons > maxCons:
            maxCons = cons
        cons = 0
if cons > maxCons:
    maxCons = cons
return maxCons 
"""

s = Solution1()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
