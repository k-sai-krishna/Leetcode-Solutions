#
# @lc app=leetcode id=2017 lang=python3
#
# [2017] Grid Game
#
from typing import *
# @lc code=start
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        up = sum(grid[0])
        down = 0
        ans = float('inf')
        for i in range(len(grid[0])):
            up -= grid[0][i]
            ans = min(ans, max(up, down))
            down = down + grid[1][i]
        return ans
        
# @lc code=end

