# -*- coding:utf-8 -*-
# @Time     : 6/21/2020 7:33 PM
# @Author   : Jupiter
# @Site     : 
# @File     : _Walls_and_Gates.py
# @Software : PyCharm

# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. Infinity means an empty room. We use the value 231 - 1 = 2147483647
# to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate.
# If it is impossible to reach a gate, it should be filled with INF.

# Example:

# Given the 2D grid:
# INF -1 0 INF
# INF INF INF -1
# INF -1 INF -1
# 0 -1 INF INF

# After running your function, the 2D grid should be:
# 3 -1 0 1
# 2 2 1 -1
# 1 -1 2 -1
# 0 -1 3 4

class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # base case:
        if not rooms:
            return
        row, col = len(rooms), len(rooms[0])
        # find the index of a gate
        q = [(i, j) for i in range(row) for j in range(col) if rooms[i][j] == 0]
        for x, y in q:
            # get the distance from a gate
            distance = rooms[x][y] + 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # That's a good a way to change direction
            for dx, dy in directions:
                # find the INF around the gate
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < row and 0 <= new_y < col and rooms[new_x][new_y] == 2147483647:
                    # update the value
                    rooms[new_x][new_y] = distance
                    q.append((new_x, new_y))  # add room in q
        return rooms


s = Solution()
print(s.wallsAndGates([[2147483647, -1, 0, 2147483647],
                       [2147483647, 2147483647, 2147483647, -1],
                       [2147483647, -1, 2147483647, -1],
                       [0, -1, 2147483647, 2147483647]]
                      ))
