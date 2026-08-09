class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:

        rows = [0] * 3
        cols = [0] * 3

        diag = 0
        anti = 0

        for i, (r, c) in enumerate(moves):

            value = 1 if i % 2 == 0 else -1

            rows[r] += value
            cols[c] += value

            if r == c:
                diag += value

            if r + c == 2:
                anti += value

            if (
                abs(rows[r]) == 3
                or abs(cols[c]) == 3
                or abs(diag) == 3
                or abs(anti) == 3
            ):
                return 'A' if value == 1 else 'B'

        if len(moves) == 9:
            return 'Draw'

        return 'Pending'