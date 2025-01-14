#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums):
            if target - num in seen:
                return ([seen[target-num],i])
            elif num not in seen:
                seen[num] = i
        
# @lc code=end

