# -*- coding:utf-8 -*-
# @Time     : 6/10/2020 9:25 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Add_Binary.py
# @Software : PyCharm

# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.

# class Solution:
#     def addBinary(self, a, b):
#         lsta = []
#         lstb = []
#         for i in a:
#             lsta.append(i)
#         for l in b:
#             lstb.append(l)
#         i ^ l
#         print(lsta)
#         print(lstb)

# just use python data format transfer method
class Solution1:
    def addBinary(self, a, b):
        # return bin(int(a,2)+int(b,2)) #0bXXXXXX
        return bin(int(a, 2) + int(b, 2))[2:]


# 1 <= a.length, b.length <= 10^4 --->05b
# Use f-string to show sum
class Solution2:
    def addBinary(self, a, b):
        sum = int(a, 2) + int(b, 2)
        return str(int(f'{sum:05b}'))


class Solution3:
    def addBinary(self, a, b):
        flag = 0

        # left-justified
        alen = len(a)
        blen = len(b)
        if alen > blen:
            b = '0' * (alen - blen) + b
        else:
            a = '0' * (blen - alen) + a

        res = ''
        for i in range(max(alen, blen) - 1, -1, -1):
            if int(a[i]) + int(b[i]) + flag >= 2:
                res = str(int(a[i]) + int(b[i]) + flag - 2) + res  # sum = 2--->0  sum=3 --> 1
                flag = 1
            else:
                res = str(int(a[i]) + int(b[i]) + flag) + res  # str(1) +'0' --> 10
                flag = 0
        else:
            if flag:
                res = '1' + res  # add flag to the top if it exceeds the original digits
        return res


s = Solution1()
print(s.addBinary("1010", "1101"))
s = Solution2()
print(s.addBinary("1010", "1101"))
s = Solution3()
print(s.addBinary("1010", "1101"))

# f-string:
# Method 1 %-formatting
# >>> name = "Eric"
# >>> age = 74
# >>> "Hello, %s. You are %s." % (name, age)
# 'Hello Eric. You are 74.'

# Method 2 str.format()
# >>> "Hello, {1}. You are {0}.".format(age, name)
# 'Hello, Eric. You are 74.'

# >>> "Hello, {}. You are {}.".format(name, age)
# 'Hello, Eric. You are 74.'

# >>> person = {'name': 'Eric', 'age': 74}
# >>> "Hello, {name}. You are {age}.".format(**person)
# 'Hello, Eric. You are 74.'

# Method 3 f-string
# >>> name = "Eric"
# >>> age = 74
# >>> f"Hello, {name}. You are {age}."
# 'Hello, Eric. You are 74.'

# Example:
# class Comedian:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} is {self.age}."
#
#     def __repr__(self):
#         return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"
# >>> new_comedian = Comedian("Eric", "Idle", "74")
# >>> f"{new_comedian}"
# 'Eric Idle is 74.'

# >>> f"{new_comedian!r}"
# 'Eric Idle is 74. Surprise!'
