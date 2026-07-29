class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        total = sum(nums)

        currmax = maxsum = nums[0]
        currmin = minsum = nums[0]

        for num in nums[1:]:

            currmax = max(num, currmax + num)
            maxsum = max(maxsum, currmax)

            currmin = min(num, currmin + num)
            minsum = min(minsum, currmin)

        if maxsum < 0:
            return maxsum

        return max(maxsum, total - minsum)
