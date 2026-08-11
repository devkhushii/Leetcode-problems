class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        nums_set = set(nums)

        # Find sequential prefix sum
        summ = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                summ += nums[i]
            else:
                break

        # Find smallest missing integer >= sum
        while summ in nums_set:
            summ += 1

        return summ

        