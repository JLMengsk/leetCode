# -*- coding:utf-8 -*-
# @Time     : 6/20/2020 5:42 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Remove_Element.py
# @Software : PyCharm

class Solution1:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)


class Solution2:
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


s = Solution1()
print(s.removeElement([3, 2, 2, 3], 3))
s = Solution2()
print(s.removeElement([3, 2, 2, 3], 3))
