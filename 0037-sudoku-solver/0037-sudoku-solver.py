class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Store existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)

                    box = (r // 3) * 3 + (c // 3)
                    boxes[box].add(num)

        def backtrack():
            for r in range(9):
                for c in range(9):

                    if board[r][c]!='.':
                        continue
                    box = (r // 3) * 3 + (c // 3)

                    for num in "123456789":
                        if (num in rows[r] or
                            num in cols[c] or
                            num in boxes[box]):
                            continue
                        
                        board[r][c]=num
                        rows[r].add(num)
                        cols[c].add(num)
                        boxes[box].add(num)

                        if backtrack():
                            return True

                        board[r][c] = "."
                        rows[r].remove(num)
                        cols[c].remove(num)
                        boxes[box].remove(num)

                    return False
            return True

        backtrack()
        