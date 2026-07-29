class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        mid = ""

        for c, f in freq.items():
            if f % 2:
                mid = c
            half[ord(c) - ord('a')] = f // 2

        m = sum(half)

        LIMIT = k

        # Count multiset permutations, stopping once we exceed k
        def ways(cnt):
            rem = sum(cnt)
            ans = 1
            for x in cnt:
                if x:
                    ans *= comb(rem, x)
                    if ans > LIMIT:
                        return LIMIT + 1
                    rem -= x
            return ans

        if ways(half) < k:
            return ""

        left = []

        for _ in range(m):

            for i in range(26):

                if half[i] == 0:
                    continue

                half[i] -= 1

                w = ways(half)

                if w >= k:
                    left.append(chr(i + ord('a')))
                    break

                k -= w
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]