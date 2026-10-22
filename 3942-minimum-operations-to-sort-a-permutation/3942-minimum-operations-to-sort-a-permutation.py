
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float('inf')

        # Check if nums follows increasing circular order
        increasing = True
        for i in range(n):
            if nums[i] != (nums[0] + i) % n:
                increasing = False
                break

        if increasing:
            k = nums[0]

            # Rotate directly, or reverse and rotate
            ans = min(ans, (n - k) % n, k + 2)

        # Check if nums follows decreasing circular order
        decreasing = True
        for i in range(n):
            if nums[i] != (nums[0] - i) % n:
                decreasing = False
                break

        if decreasing:
            k = (n - 1 - nums[0]) % n

            # Reverse, then choose the cheaper rotation
            ans = min(ans, 1 + k, 1 + (n - k) % n)

        if ans == float('inf'):
            return -1

        return ans
