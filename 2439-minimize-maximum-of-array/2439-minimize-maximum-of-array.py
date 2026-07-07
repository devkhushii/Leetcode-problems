class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        answer = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            current = (prefix_sum + i) // (i + 1)

            answer = max(answer, current)

        return answer