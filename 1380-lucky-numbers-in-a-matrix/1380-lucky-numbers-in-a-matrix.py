class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        row = len(matrix)
        col = len(matrix[0])

        result = []

        for i in range(row):

            min_row = min(matrix[i])
            j = matrix[i].index(min_row)

            max_col = max(matrix[k][j] for k in range(row))

            if min_row == max_col:
                result.append(min_row)

        return result
            
        