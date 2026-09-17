class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        best = [INF] * n

        left = 0
        total = 0
        answer = INF
        min_length = INF

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, length + best[left - 1])

                min_length = min(min_length, length)

            best[right] = min_length

        return -1 if answer == INF else answer     