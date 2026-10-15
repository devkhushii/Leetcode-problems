
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i, n):
                subarray = nums[i:j + 1]
                distinct_count = len(set(subarray))
                ans += distinct_count ** 2

        return ans

        