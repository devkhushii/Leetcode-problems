class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with num
            new_dp[num % k] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r]:
                    new_r = (r * num) % k
                    new_dp[new_r] += dp[r]

            dp = new_dp

            # Add all subarrays ending here
            for r in range(k):
                ans[r] += dp[r]

        return ans