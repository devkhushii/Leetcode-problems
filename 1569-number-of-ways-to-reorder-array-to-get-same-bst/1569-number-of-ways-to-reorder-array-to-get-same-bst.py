from math import comb
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def dfs(arr):
            # An empty or single-node tree has one arrangement
            if len(arr) <= 2:
                return 1

            root = arr[0]

            # Split values into left and right subtrees
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            # Count ways to interleave left and right nodes
            ways = comb(len(left) + len(right), len(left))

            # Multiply by the valid arrangements of both subtrees
            ways *= dfs(left)
            ways *= dfs(right)

            return ways % MOD

        # Exclude the original ordering itself
        return (dfs(nums) - 1) % MOD