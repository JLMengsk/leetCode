# -*- coding:utf-8 -*-
# @Time     : 6/13/2020 12:22 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Two_Sum_II.py
# @Software : PyCharm

# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.


# This one could use hash table and BS

# Very Slow
class Solution1:
    def twoSum(self, numbers, target):
        for i in numbers:
            a = target - i
            if a == i:
                return [numbers.index(i) + 1, numbers.index(i) + 2]
            if a in numbers:
                return [numbers.index(i) + 1, numbers.index(target - i) + 1]


# Two pointer
class Solution2:
    def twoSum(self, numbers, target):
        N = len(numbers)
        left, right = 0, N - 1
        while left < right:
            cursum = numbers[left] + numbers[right]
            if cursum == target:
                return [left + 1, right + 1]
            elif cursum < target:
                left += 1  # left is always smaller than right
            else:
                right -= 1
        return [0, 0]


# Binary Search
class Solution3:
    def twoSum(self, numbers, target):
        def bsearch(left, right, t): # t is target
            if left > right:
                return -1
            l, r = left, right
            while l <= r:
                mid = l + (r-l) // 2
                if numbers[mid] == t:
                    return mid
                elif numbers[mid] > t:
                    r = mid -1
                else:
                    l = mid +1
            return -1
        for i, n in enumerate(numbers):
            idx = bsearch(i+1,len(numbers)-1,target-n)
            if idx != -1:
                return [i+1,idx+1]
        return [-1]
# Another way BS
        # for i in range(len(numbers)):
        #     x = target - numbers[i]
        #     left = i + 1  # i almost been minused
        #     right = len(numbers) - 1
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if numbers[mid] == x:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] < x:
        #             left = mid + 1
        #         else:
        #             right = mid - 1

# Hash Table
class Solution4:
    def twoSum(self, numbers, target):
        dict1 = {}
        for i in range(len(numbers)):
            if numbers[i] in dict1:
                return [dict1[numbers[i]], i + 1]  # dict1[numbers[i]](key) return to the index(value)
            # i + 1 means this time index
            else:
                x = target - numbers[i]  # store each result in the dict
                dict1[x] = i + 1  # return answer index starts at 1, so plus one


s = Solution1()
print(s.twoSum([2, 7, 11, 15], 9))
s = Solution2()
print(s.twoSum([2, 7, 11, 15], 9))
s = Solution3()
print(s.twoSum([2, 7, 11, 15], 9))
s = Solution4()
print(s.twoSum([2, 7, 11, 15], 22))
