# -*- coding:utf-8 -*-
# @Time     : 6/21/2020 8:47 PM
# @Author   : Jupiter
# @Site     : 
# @File     : Number_of_Islands.py
# @Software : PyCharm

import collections


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
                    self.islandErase(grid, i, j)
                    count += 1
        return count

    def islandErase(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.islandErase(grid, i - 1, j)
        self.islandErase(grid, i + 1, j)
        self.islandErase(grid, i, j - 1)
        self.islandErase(grid, i, j + 1)


class Solution2:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        M, N = len(grid), len(grid[0])
        que = collections.deque()
        res = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    que.append((i, j))
                    while que:
                        x, y = que.pop()
                        for d in directions:
                            nx, ny = x + d[0], y + d[1]
                            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                que.append((nx, ny))
        return res


s = Solution()
print(s)
