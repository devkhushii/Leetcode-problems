class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}

        # Count frequency
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        # Sort frequencies in descending order
        frequencies = sorted(freq.values(), reverse=True)

        pushes = 0

        for i, f in enumerate(frequencies):
            pushes += (i // 8 + 1) * f

        return pushes
        