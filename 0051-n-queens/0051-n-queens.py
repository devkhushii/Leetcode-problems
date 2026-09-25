class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board= [['.'] * n for _ in range(n)]
        ans=[]
        def isSafe(board,row,col,n):

            for j in range(n):
                if board[row][j]=='Q':
                    return False
                
            for i in range(n):
                if board[i][col]=='Q':
                    return False
            
            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i = row - 1
            j = col + 1

            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def nQueens(board,row,n,ans):
            if row==n:
                ans.append([''.join(row) for row in board])
                return
            
            for j in range(n):
                if isSafe(board,row,j,n):
                    board[row][j]='Q'
                    nQueens(board,row+1,n,ans)
                    board[row][j]='.'
        
        nQueens(board,0,n,ans)
        return ans