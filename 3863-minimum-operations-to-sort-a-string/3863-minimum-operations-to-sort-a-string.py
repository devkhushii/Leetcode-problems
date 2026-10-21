
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Already sorted
        if s == ''.join(sorted(s)):
            return 0

        # Cannot sort the entire string in one operation
        if n == 2:
            return -1

        smallest = min(s)
        largest = max(s)

        # One operation is enough
        if s[0] == smallest or s[-1] == largest:
            return 1

        # If smallest or largest is in the middle,
        # two operations are enough
        for i in range(1, n - 1):
            if s[i] == smallest or s[i] == largest:
                return 2

        # Otherwise, three operations are enough
        return 3
