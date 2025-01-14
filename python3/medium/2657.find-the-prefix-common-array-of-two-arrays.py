#
# @lc app=leetcode id=2657 lang=python3
#
# [2657] Find the Prefix Common Array of Two Arrays
#

# @lc code=start
from typing import *
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # approach 1
        # n = len(A)
        # ans = [0]*n
        # freq = [0]*(n+1) # since in permutation numbers lies in range [1,n]
        # common = 0
        # for i in range(n):
        #     freq[A[i]] += 1
        #     if freq[A[i]] == 2:
        #         common += 1
        #     freq[B[i]] += 1
        #     if freq[B[i]] == 2:
        #         common += 1
        #     ans[i] = common
        # return ans

        # approach 2
        n = len(A)
        inA = set()
        inB = set()
        ans = [0]*n
        for i in range(n):
            inA.add(A[i])
            inB.add(B[i])
            c = 0
            for e in inA:
                if e in inB:
                    c += 1
            ans[i] = c
        return ans
# @lc code=end

