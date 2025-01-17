#
# @lc app=leetcode id=3223 lang=python3
#
# [3223] Minimum Length of String After Operations
#

# @lc code=start
from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        for val in freq.values():
            if val & 1 == 0:
                ans += 2
            else:
                ans += 1
        return ans

# @lc code=end

