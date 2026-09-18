class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence of every character
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Try to create a valid interval for each character
        for ch in range(26):
            if first[ch] == n:
                continue

            left = first[ch]
            right = last[ch]

            i = left
            valid = True

            while i <= right:
                idx = ord(s[i]) - ord('a')

                # This character occurs before our left boundary
                if first[idx] < left:
                    valid = False
                    break

                right = max(right, last[idx])
                i += 1

            if valid:
                intervals.append((left, right))

        # Earliest ending interval first
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result