class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        n=len(image)
        m=len(image[0])
        original_color=image[sr][sc]
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m or image[i][j]==color or image[i][j]!=original_color:
                return
            
            image[i][j]=color
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        # for i in range(n):
        #     for j in range(m):
        #         if image[i][j]==original_color:
        dfs(sr,sc)
        return image