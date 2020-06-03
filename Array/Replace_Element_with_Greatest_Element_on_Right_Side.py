# -*- coding:utf-8 -*-
# @Time     : 6/3/2020 7:49 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Replace_Element_with_Greatest_Element_on_Right_Side.py
# @Software : PyCharm
class Solution:
    def replaceElements(self, arr):
        for i in range(0, len(arr) - 1):
            arr[i] = max(arr[i + 1:])
        arr[-1] = -1
        return arr


s = Solution()
print(s.replaceElements([17, 18, 5, 4, 6, 1]))
