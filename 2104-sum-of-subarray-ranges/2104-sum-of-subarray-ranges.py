class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        s = 0

        for i in range(len(nums)):
            maxi = nums[i]
            mini = nums[i]

            for j in range(i, len(nums)):
                maxi = max(maxi, nums[j])
                mini = min(mini, nums[j])

                s += maxi - mini

        return s
        