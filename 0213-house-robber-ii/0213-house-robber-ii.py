
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_linear(houses):
            m = len(houses)
            dp = [0] * m

            dp[0] = houses[0]

            if m == 1:
                return dp[0]

            dp[1] = max(houses[0], houses[1])

            for i in range(2, m):
                # Either skip this house or rob it
                dp[i] = max(dp[i - 1],
                            dp[i - 2] + houses[i])

            return dp[m - 1]

        # Case 1: Exclude the last house
        case1 = rob_linear(nums[:-1])

        # Case 2: Exclude the first house
        case2 = rob_linear(nums[1:])

        return max(case1, case2)
