class Solution:
    def findSubsequences(self,nums, i, current, current_sum, target, result):

        # BASE CASE
        if i == len(nums):
            if current_sum == target:
                result.append(current.copy())
            return
        if i == len(nums) or current_sum > target:
            return
        # TAKE
        current.append(nums[i])
        current_sum += nums[i]

        self.findSubsequences(
            nums, i , current, current_sum, target, result
        )

        # UNDO
        current.pop()
        current_sum -= nums[i]

        # DON'T TAKE
        self.findSubsequences(
            nums, i + 1, current, current_sum, target, result
        )

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        current_sum=0
        current=[]
        self.findSubsequences(candidates, 0, current, current_sum, target, result)
        return result

        