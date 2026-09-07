class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26
        total = 0

        for ch in s:
            index = ord(ch) - ord('a')

            new_subsequences = total + 1

            total = (total + new_subsequences - dp[index]) % MOD

            dp[index] = new_subsequences

        return total