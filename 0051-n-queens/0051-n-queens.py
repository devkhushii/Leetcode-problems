# class Solution:
#     def solveNQueens(self, n: int) -> list[list[str]]:

#         board = [['.'] * n for _ in range(n)]
#         ans = []

#         def isSafe(board, row, col, n):

#             # Check same row
#             for j in range(n):
#                 if board[row][j] == 'Q':
#                     return False

#             # Check same column
#             for i in range(n):
#                 if board[i][col] == 'Q':
#                     return False

#             # Check upper-left diagonal
#             i = row - 1
#             j = col - 1

#             while i >= 0 and j >= 0:
#                 if board[i][j] == 'Q':
#                     return False
#                 i -= 1
#                 j -= 1

#             # Check upper-right diagonal
#             i = row - 1
#             j = col + 1

#             while i >= 0 and j < n:
#                 if board[i][j] == 'Q':
#                     return False
#                 i -= 1
#                 j += 1

#             return True

#         def nQueens(board, row, n, ans):

#             if row == n:
#                 ans.append([''.join(row) for row in board])
#                 return

#             for j in range(n):

#                 if isSafe(board, row, j, n):

#                     # Choose
#                     board[row][j] = 'Q'

#                     # Explore
#                     nQueens(board, row + 1, n, ans)

#                     # Undo
#                     board[row][j] = '.'

#         nQueens(board, 0, n, ans)

#         return ans

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.'] * n for _ in range(n)]
        ans = []

        cols = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        def backtrack(row):
            if row == n:
                ans.append([''.join(r) for r in board])
                return

            for col in range(n):

                # Check column and diagonals in O(1)
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Choose
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Explore
                backtrack(row + 1)

                # Undo
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return ans