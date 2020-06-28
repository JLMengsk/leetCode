# -*- coding:utf-8 -*-
# @Time     : 6/24/2020 8:54 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Number_of_Islands.py
# @Software : PyCharm

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# DFS
class Solution:
    def numIslands(self, grid):
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = "0"
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                if grid[nr][nc] == '1':
                    self.dfs(grid, nr, nc)


s = Solution()
print(s)
