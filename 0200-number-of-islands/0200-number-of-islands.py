class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for _ in range(n)]

        def dfs(i,j,vis,grid,n,m):
            if i<0 or j<0 or i>=n or j>=m or vis[i][j] or grid[i][j]!='1':
                return

            vis[i][j]=True
            dfs(i-1,j,vis,grid,n,m)
            dfs(i,j+1,vis,grid,n,m)
            dfs(i+1,j,vis,grid,n,m)
            dfs(i,j-1,vis,grid,n,m)

        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and not vis[i][j]:
                    dfs(i,j,vis,grid,n,m)
                    islands+=1
        return islands
