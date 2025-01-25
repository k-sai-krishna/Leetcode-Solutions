#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#
from typing import List
# @lc code=start
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_count = [0]*len(grid)
        col_count = [0]*len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    row_count[row] += 1
                    col_count[col] += 1
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] and (row_count[row] > 1 or col_count[col] > 1):
                    ans += 1
        return ans
# @lc code=end

