class Solution:
    def findCombinations(self, candidates, start, current, current_sum, target, result):

        # BASE CASE
        if current_sum == target:
            result.append(current.copy())
            return

        if current_sum > target:
            return

        for i in range(start, len(candidates)):

            # Skip duplicate values at the same recursion level
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            # TAKE
            current.append(candidates[i])
            current_sum += candidates[i]

            # i + 1 because each element can be used only once
            self.findCombinations(
                candidates,
                i + 1,
                current,
                current_sum,
                target,
                result
            )

            # UNDO
            current.pop()
            current_sum -= candidates[i]

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        result = []
        current = []

        self.findCombinations(
            candidates,
            0,
            current,
            0,
            target,
            result
        )

        return result
        