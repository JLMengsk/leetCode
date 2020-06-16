# -*- coding:utf-8 -*-
# @Time     : 6/13/2020 8:10 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Rotate_Array.py
# @Software : PyCharm

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# class wrong_Solution:
#     def rotate(self, nums, k):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         return nums.append(nums.pop)

class Solution1:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = k % len(nums)  # k may bigger than len(nums)
        nums[:] = nums[-i:] + nums[:-i]
        return nums


# Approach 1: Brute Force
# The simples approach is to rotate all the elements of the array in kk steps
# by rotating the elements by 1 unit in each step.
class Solution2:
    def rotate(self, nums, k):
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):  # do len(nums)-1 times
                nums[j], previous = previous, nums[j]
        return nums


# Approach 2: Using Extra Array
# We use an extra array in which we place every element of the array at its correct position
# i.e. the number at index ii in the original array is placed at the index (i + k) %
# length of array. Then, we copy the new array to the original one.
class Solution3:
    def rotate(self, nums, k):
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a
        return nums


# Approach 3: Using Cyclic Replacements
"""
We can directly place every number of the array at its required correct position. 
But if we do that, we will destroy the original element. 
Thus, we need to store the number being replaced in a temp variable. 
Then, we can place the replaced number(temp) at its correct position and so on,n times,where n is the length of array.
We have chosen nn to be the number of replacements since we have to shift all the elements of the array(which is nn). 
But, there could be a problem with this method, if n % k = 0 
where k = k % n (since a value of k larger than n eventually leads to a k equivalent to k % n). 
In this case, while picking up numbers to be placed at the correct position, 
we will eventually reach the number from which we originally started. 
Thus, in such a case, when we hit the original number's index again, 
we start the same process with the number following it.

Now let's look at the proof of how the above method works. Suppose, we have n as the number of elements in the array 
and k is the number of shifts required. 
Further, assume n % k = 0.
Now, when we start placing the elements at their correct position, 
in the first cycle all the numbers with their index i satisfying i %k = 0 get placed at their required position.
This happens because when we jump k steps every time, we will only hit the numbers k steps apart.
We start with index i = 0, having i % k = 0. 
Thus, we hit all the numbers satisfying the above condition in the first cycle. 
When we reach back the original index, we have placed n/k elements at their correct position, 
since we hit only that many elements in the first cycle. 
Now, we increment the index for replacing the numbers. This time, we place other  n/k elements at their correct position, 
different from the ones placed correctly in the first cycle, 
because this time we hit all the numbers satisfy the condition i % k = 1. 
When we hit the starting number again, we increment the index and repeat the same process from i = 1 
for all the indices satisfying i % k == 1. 
This happens till we reach the number with the index i % k = 0 again,
which occurs for i=k. 
We will reach such a number after a total of k cycles. 
Now, the total count of numbers exclusive numbers placed at their correct position will be k * (n/k) = n
Thus, all the numbers will be placed at their correct position.
"""
# class Solution4:
#     def rotate(self, nums, k):
#         n = len(nums)
#         k %= n
#
#         start = count = 0
#         while count < 0:
#             current, prev = start, nums[start]
#             while True:
#                 next_idx = (current + k) % n
#                 nums[next_idx], prev = prev, nums[next_idx]
#                 current = next_idx
#                 count += 1
#
#                 if start == current:
#                     break
#             start += 1


s = Solution1()
print(s.rotate([-1, -100, 3, 99], 2))
s = Solution2()
print(s.rotate([1, 2, 3, 4, 5, 6, 7], 1))
s = Solution3()
print(s.rotate([1, 2, 3, 4, 5, 6, 7], 1))
s = Solution4()
print(s.rotate([1, 2, 3, 4, 5, 6, 7], 1))
