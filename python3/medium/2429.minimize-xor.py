#
# @lc app=leetcode id=2429 lang=python3
#
# [2429] Minimize XOR
#

# @lc code=start
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ans = num1
        i = 0
        ans_count = ans.bit_count()
        num2_count = num2.bit_count()
        while ans_count < num2_count:
            if not ans & (1 << i):
                ans = ans | (1 << i)
                ans_count += 1
            i += 1
        while ans_count > num2_count:
            if ans & (1 << i):
                ans = ans & ~(1 << i)
                ans_count -= 1
            i += 1
        return ans
# @lc code=end

