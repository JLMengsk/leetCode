# -*- coding:utf-8 -*-
# @Time     : 6/12/2020 8:43 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Reverse_String.py
# @Software : PyCharm

# Write a function that reverses a string. The input string is given as an array of characters char[].

class Solution1:
    def reverseString(self, s):
        return s[::-1]
    # or
    #   s.reverse()

# Two Pointers, Iteration, O(1) Space
class Solution2:
    def reverseString(self, s):
        i = 0
        j = len(s) - 1
        # if i != j and  i != (len(s)-1)/2:X
        # if i != j:X
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


class Solution3:
    def reverseString(self, s):
        lst = []
        for i in range(len(s)):
            lst.append(s.pop())
        return lst


# Recursion, In-Place, O(N)Space
class Solution4:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


s = Solution1()
print(s.reverseString(["h", "e", "l", "l", "o"]))
s = Solution2()
print(s.reverseString(["h", "e", "l", "l", "o"]))
s = Solution3()
print(s.reverseString(["h", "e", "l", "l", "o"]))
s = Solution4()
print(s.reverseString(["h", "e", "l", "l", "o"]))


"""
1. 简单的步长为-1, 即字符串的翻转(常用);
def string_reverse1(string):
    return string[::-1]
    
2. 交换前后字母的位置;
def string_reverse2(string):
    t = list(string)
    l = len(t)
    for i,j in zip(range(l-1, 0, -1), range(l//2)):
        t[i], t[j] = t[j], t[i]
    return "".join(t)
    
3. 递归的方式, 每次输出一个字符;
def string_reverse3(string):
    if len(string) <= 1:
        return string
    return string_reverse3(string[1:]) + string[0]
    
4. 双端队列, 使用extendleft()函数;
from collections import deque
def string_reverse4(string):
    d = deque()
    d.extendleft(string)
    return ''.join(d)
    
5. 使用for循环, 从左至右输出;
def string_reverse5(string):
    #return ''.join(string[len(string) - i] for i in range(1, len(string)+1))
    return ''.join(string[i] for i in range(len(string)-1, -1, -1))
"""
