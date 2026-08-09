class Solution:
    def main_diagonal(self,matrix):
        return [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]

    def anti_diagonal(self,matrix):
        n = len(matrix)
        return [matrix[i][n - 1 - i] for i in range(n)]

    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        if n%2==0:
            return (sum(self.main_diagonal(mat))+sum(self.anti_diagonal(mat)))
        else:
            mid=n//2
            return (sum(self.main_diagonal(mat))+sum(self.anti_diagonal(mat))-mat[mid][mid])
        