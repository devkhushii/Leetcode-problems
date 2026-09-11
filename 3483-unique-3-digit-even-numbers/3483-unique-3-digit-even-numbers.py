class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10

        for digit in digits:
            freq[digit] += 1

        ans = 0

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            count = [0] * 10

            for digit in (a, b, c):
                count[digit] += 1

            if all(count[i] <= freq[i] for i in range(10)):
                ans += 1

        return ans