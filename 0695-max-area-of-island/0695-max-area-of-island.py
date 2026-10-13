class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area=0
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for _ in range(n)]
        area=[0]

        def dfs(i,j,vis,grid,n,m):
            
            if i<0 or j<0 or i>=n or j>=m or vis[i][j] or grid[i][j]!=1:
                return 0
           
            vis[i][j]=True
            return (1+dfs(i-1,j,vis,grid,n,m)+
            dfs(i,j+1,vis,grid,n,m)+
            dfs(i+1,j,vis,grid,n,m)+
            dfs(i,j-1,vis,grid,n,m))

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    max_area=max(max_area,dfs(i,j,vis,grid,n,m))
                    
        return max_area
