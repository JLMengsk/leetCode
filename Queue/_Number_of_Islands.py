# -*- coding:utf-8 -*-
# @Time     : 6/21/2020 8:47 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Number_of_Islands.py
# @Software : PyCharm

class Solution:
    def numIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.islandErase(grid,i,j)
                    count += 1
        return count

    def islandErase(self,grid,i,j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.islandErase(grid, i - 1, j)
        self.islandErase(grid, i + 1, j)
        self.islandErase(grid, i, j - 1)
        self.islandErase(grid, i, j + 1)


s = Solution()
print(s)
