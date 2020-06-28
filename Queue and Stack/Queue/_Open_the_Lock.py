# -*- coding:utf-8 -*-
# @Time     : 6/22/2020 4:45 PM
# @Author   : Jupiter
# @Site     : 
# @File     : _Open_the_Lock.py
# @Software : PyCharm


# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6',
# '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be
# '9'. Each move consists of turning one wheel one slot. The lock initially starts at '0000', a string representing
# the state of the 4 wheels.
#
# You are given a list of deadends dead ends,
# meaning if the lock displays any of these codes,
# the wheels of the lock will stop turning and you will be unable to open it.
#
# Given a target representing the value of the wheels that will unlock the lock,
# return the minimum total number of turns required to open the lock, or -1 if it is impossible.
import collections


class Solution1:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadset = set(deadends)
        if (target in deadset) or ("0000" in deadset): return -1
        que = collections.deque()
        que.append("0000")
        visited = set(["0000"])
        step = 0
        while que:
            step += 1
            size = len(que)
            for i in range(size):
                point = que.popleft()
                for j in range(4):
                    for k in range(-1, 2, 2):
                        newPoint = [i for i in point]
                        newPoint[j] = chr((ord(newPoint[j]) - ord('0') + k + 10) % 10 + ord('0'))
                        """
                        >>>ord('a')
                        97
                        >>> print chr(48), chr(49), chr(97)         # 十进制
                        0 1 a
                        """
                        newPoint = "".join(newPoint)
                        if newPoint == target:
                            return step
                        if (newPoint in deadset) or (newPoint in visited):
                            continue
                        que.append(newPoint)
                        visited.add(newPoint)
        return -1


class Solution2:
    def openLock(self, deadends, target):
        dead_set = set(deadends)
        queue = collections.deque()
        queue.append(('0000', 0))
        visited = set('0000')
        while queue:
            string, step = queue.popleft()
            if string in dead_set:
                continue
            if string == target:
                return step
            for i in range(4):
                num = int(string[i])
                for dx in (-1, 1):
                    num_new = (num + dx) % 10  # -1%10=9
                    string_new = string[:i] + str(num_new) + string[i + 1:]
                    # print(string_new)
                    if string_new not in visited:
                        queue.append((string_new, step + 1))
                        visited.add(string_new)
        return -1


s = Solution1()
print(s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
s = Solution2()
print(s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
