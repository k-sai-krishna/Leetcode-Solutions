#
# @lc app=leetcode id=2661 lang=python3
#
# [2661] First Completely Painted Row or Column
#
from typing import *
# @lc code=start
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        numsToPos = {}
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                numsToPos[mat[row][col]] = (row, col)
        row_count = [0]*len(mat)
        col_count = [0]*len(mat[0])
        for i in range(len(arr)):
            row, col = numsToPos[arr[i]]
            row_count[row] += 1
            col_count[col] += 1
            if row_count[row] == len(mat[0]) or col_count[col] == len(mat):
                return i

# @lc code=end

