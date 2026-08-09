class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:

        board = [[' ' for _ in range(3)] for _ in range(3)]

        # Build the board
        for i, (r, c) in enumerate(moves):
            board[r][c] = 'X' if i % 2 == 0 else 'O'

        # Check rows
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return 'A' if board[i][0] == 'X' else 'B'

        # Check columns
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != ' ':
                return 'A' if board[0][j] == 'X' else 'B'

        # Main diagonal
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return 'A' if board[0][0] == 'X' else 'B'

        # Anti-diagonal
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return 'A' if board[0][2] == 'X' else 'B'

        # No winner
        if len(moves) == 9:
            return 'Draw'

        return 'Pending'