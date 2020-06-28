# -*- coding:utf-8 -*-
# @Time     : 6/22/2020 8:04 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Perfect_Squares.py
# @Software : PyCharm

# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

from collections import deque

"""
借助队列实现广度优先遍历（层次遍历）

初始化队列queue=[n]queue=[n]queue=[n]，访问元组visited={}visited=\{\}visited={}，初试化路径长度step=0step=0step=0

特判，若n==0n==0n==0，返回000。

循环条件，队列不为空：

step+=1step+=1step+=1，因为循环一次，意味着一层中的节点已经遍历完，所以路径长度需要加一。
定义当前层中的节点数l=len(queue)l=len(queue)l=len(queue)，遍历当前层的所有节点：
令tmptmptmp为队首元素。
遍历所有可能数iii的平方数，遍历区间[1,int(tmp−−−−√)+1)[1,int(\sqrt{tmp})+1)[1,int( 
tmp
​	
 )+1)：
定义x=tmp−i2x=tmp-i^{2}x=tmp−i 
2
 
若x==0x==0x==0，返回当前的路径长度。
若x not in visitedx\ not\ in\ visitedx not in visited，表示当前节点未出现过：将该节点入队并在访问数组中加入。
"""


class Solution1:
    def numSquares(self, n):
        if n == 0:
            return 0
        queue = deque([n])
        step = 0
        visited = set()
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                tmp = queue.popleft()
                for i in range(1, int(tmp ** 0.5) + 1):
                    x = tmp - i ** 2
                    if x == 0:
                        return step
                    if x not in visited:
                        queue.append(x)
                        visited.add(x)
        return step

# 四平方和定理
class Solution2:
    def numSquares(self, n):
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4

        squares = set()
        i = 1
        while i * i <= n:
            squares.add(i*i)
            i += 1
        if n in squares:
            return 1
        if any(n - x in squares for x in squares):
            return 2
        return 3
s = Solution1()
print(s.numSquares(12))
