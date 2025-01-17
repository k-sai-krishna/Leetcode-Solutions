#
# @lc app=leetcode id=2116 lang=python3
#
# [2116] Check if a Parentheses String Can Be Valid
#

# @lc code=start
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1 == 1:
            return False
        locked_open = []
        unlocked = []
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                locked_open.append(i)
            else:
                if s[i] == ')':
                    if locked_open:
                        locked_open.pop()
                    elif unlocked:
                        unlocked.pop()
                    else:
                        return False
        while locked_open and unlocked and locked_open[-1] < unlocked[-1]:
            locked_open.pop()
            unlocked.pop()
        return not locked_open

        
# @lc code=end

