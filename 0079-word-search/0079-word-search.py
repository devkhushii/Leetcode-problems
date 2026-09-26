class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def backtrack(i, j, index):
            if index == len(word):
                return True
            
            if (
                i < 0 or i >= rows or
                j < 0 or j >= cols or
                (i, j) in visited or
                board[i][j] != word[index]
            ):
                return False

            visited.add((i, j))

            if (backtrack(i - 1, j, index + 1)  or
                backtrack(i + 1, j, index + 1)  or
                backtrack(i, j - 1, index + 1)  or
                backtrack(i, j + 1, index + 1)  ):

                return True
            visited.remove((i,j))
            return False

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False


            
            
            

        