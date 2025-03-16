#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
from typing import *
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def lower_bound(nums, target):
            ans = len(nums)
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] >= target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans
        def upper_bound(nums, target):
            ans = len(nums)
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] > target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans
        return lower_bound(nums, target)
# @lc code=end

