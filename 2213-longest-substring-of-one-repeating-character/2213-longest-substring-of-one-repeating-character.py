#SOLVED BY ai
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:

        n = len(s)

        # left char, right char,
        # prefix length, suffix length, best length
        tree = [None] * (4 * n)

        def merge(a, b, left_len, right_len):
            a_left, a_right, a_pre, a_suf, a_best = a
            b_left, b_right, b_pre, b_suf, b_best = b

            pre = a_pre
            suf = b_suf
            best = max(a_best, b_best)

            if a_right == b_left:
                best = max(best, a_suf + b_pre)

                if a_pre == left_len:
                    pre = a_pre + b_pre

                if b_suf == right_len:
                    suf = a_suf + b_suf

            return (a_left, b_right, pre, suf, best)

        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1],
                mid - l + 1,
                r - mid
            )

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = (char, char, 1, 1, 1)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1],
                mid - l + 1,
                r - mid
            )

        build(1, 0, n - 1)

        ans = []

        for i in range(len(queryIndices)):
            update(
                1,
                0,
                n - 1,
                queryIndices[i],
                queryCharacters[i]
            )

            ans.append(tree[1][4])

        return ans