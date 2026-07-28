class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26

        # Count frequency
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        left = []
        middle = ""

        # Build left half
        for i in range(26):
            left.extend(chr(ord('a') + i) * (freq[i] // 2))

            if freq[i] % 2 == 1:
                middle = chr(ord('a') + i)

        left = "".join(left)
        right = left[::-1]

        return left + middle + right