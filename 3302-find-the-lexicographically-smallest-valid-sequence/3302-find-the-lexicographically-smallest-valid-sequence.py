class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # suf[i] = number of characters from word2 that can
        # be matched exactly using word1[i:]
        suf = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1

            suf[i] = m - 1 - j

        # Build answer greedily
        ans = []
        j = 0
        used_mismatch = False

        for i in range(n):
            if len(ans) == m:
                break

            if word1[i] == word2[j]:
                # Exact match
                ans.append(i)
                j += 1

            elif not used_mismatch:
                # Use our one allowed mismatch.
                #
                # After taking word1[i], we need to match
                # word2[j+1:] exactly.
                remaining = m - (j + 1)

                if suf[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
                    used_mismatch = True

        if len(ans) == m:
            return ans

        return []
        