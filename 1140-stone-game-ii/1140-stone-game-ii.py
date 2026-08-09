class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp(i, M) = maximum stones current player can get
        # from piles[i:] when M is M
        memo = {}

        def dp(i, M):
            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            for X in range(1, 2 * M + 1):
                next_i = i + X
                next_M = max(M, X)

                # Total remaining - what opponent can get
                current = suffix[i] - dp(next_i, next_M)

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)