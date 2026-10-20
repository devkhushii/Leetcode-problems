
class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        # prefix maximum: largest element before index i
        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        # suffix minimum: smallest element from index i onward
        suff_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])

        # Count adjacent decreases up to each index
        drops = [0] * n
        for i in range(1, n):
            drops[i] = drops[i - 1] + (nums[i - 1] > nums[i])

        ans = 0

        # k must divide n
        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            # Check every block of length k
            for start in range(0, n, k):
                end = start + k - 1

                # Number of decreases inside this block
                internal_drops = drops[end] - drops[start]

                # A circular block can be sorted by rotation
                # if it has at most one circular decrease.
                circular_drop = nums[end] > nums[start]

                if internal_drops + circular_drop > 1:
                    valid = False
                    break

                # All earlier blocks must contain values
                # no greater than all values in this block
                if pref_max[start] > suff_min[start]:
                    valid = False
                    break

            if valid:
                ans += k

        return ans
