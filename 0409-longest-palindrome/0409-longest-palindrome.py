class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        ans = 0
        odd = False

        for value in freq.values():
            if value % 2 == 0:
                ans += value
            else:
                ans += value - 1
                odd = True

        if odd:
            ans += 1

        return ans
            