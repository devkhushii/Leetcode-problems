class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        is_pal = [[False] * n for _ in range(n)]

        # Check all substrings for palindrome
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't select a palindrome ending at i - 1
            dp[i] = dp[i - 1]

            # Try every possible starting position
            for j in range(i - k + 1):
                if i - j >= k and is_pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]