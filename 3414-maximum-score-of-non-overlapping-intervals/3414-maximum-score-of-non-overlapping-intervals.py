class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted(
            [(s, e, w, i) for i, (s, e, w) in enumerate(intervals)],
            key=lambda x: x[1]
        )

        n = len(intervals)
        ends = [x[1] for x in intervals]

        # prev[i] = last interval that ends before intervals[i] starts
        prev = []
        for i in range(n):
            s = intervals[i][0]

            lo, hi = 0, i
            while lo < hi:
                mid = (lo + hi) // 2
                if ends[mid] < s:
                    lo = mid + 1
                else:
                    hi = mid

            prev.append(lo - 1)

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            s, e, w, idx = intervals[i - 1]

            for k in range(1, 5):
                # Don't take current interval
                best = dp[i - 1][k]

                # Take current interval
                p = prev[i - 1] + 1
                take_score = dp[p][k - 1][0] + w
                take_indices = sorted(dp[p][k - 1][1] + [idx])

                if take_score > best[0] or (
                    take_score == best[0] and take_indices < best[1]
                ):
                    best = (take_score, take_indices)

                dp[i][k] = best

        return dp[n][4][1]