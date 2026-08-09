class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        if row * col != r * c:
            return mat

        reshape = [[0] * c for _ in range(r)]

        for index in range(row * col):
            old_i = index // col
            old_j = index % col

            new_i = index // c
            new_j = index % c

            reshape[new_i][new_j] = mat[old_i][old_j]

        return reshape