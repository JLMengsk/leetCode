# -*- coding:utf-8 -*-
# @Time     : 6/2/2020 8:40 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Remove_Element.py
# @Software : PyCharm

# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Just use Python way
class Solution1:
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)


class Solution2:
    def removeElement(self, nums, val):
        index = 0
        count = 0
        for i in nums:
            if (i != val):
                count += 1
                nums[index] = i
                index += 1
        return count


s = Solution1()
print(s.removeElement([3, 2, 2, 3], 3))
s = Solution2()
print(s.removeElement([3, 2, 2, 3], 3))
