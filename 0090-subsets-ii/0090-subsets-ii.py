class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        current = []

        def backtrack(start):
            result.append(current.copy())

            for i in range(start, len(nums)):

                # Skip duplicate at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # TAKE
                current.append(nums[i])

                backtrack(i + 1)

                # UNDO
                current.pop()

        backtrack(0)

        return result
        