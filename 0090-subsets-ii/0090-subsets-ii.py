class Solution:
    def backtrack(self, nums, start, ans, sub):
        sub.append(ans.copy())

        for i in range(start, len(nums)):

            if i > start and nums[i] == nums[i - 1]:
                continue

            ans.append(nums[i])

            self.backtrack(nums, i + 1, ans, sub)

            ans.pop()

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        sub = []
        ans = []

        self.backtrack(nums, 0, ans, sub)

        return sub
        