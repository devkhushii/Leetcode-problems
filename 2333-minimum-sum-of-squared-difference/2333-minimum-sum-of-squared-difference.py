class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        # Find the smallest maximum difference we can achieve
        while left < right:
            mid = (left + right) // 2
            needed = sum(max(d - mid, 0) for d in diff)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        # Reduce all differences greater than left down to left
        remaining = k - sum(max(d - left, 0) for d in diff)

        ans = 0
        for d in diff:
            d = min(d, left)

            # Use remaining operations to reduce some values by one more
            if d == left and remaining > 0:
                d -= 1
                remaining -= 1

            ans += d * d

        return ans
