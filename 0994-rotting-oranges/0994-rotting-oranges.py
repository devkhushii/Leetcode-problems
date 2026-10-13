class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        sources=deque()
        n=len(grid)
        m=len(grid[0])
        vis=[[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    sources.append((i,j,0))  
                    # vis[i][j]=True
       
        ans=0
        
        while sources:
            i,j,t=sources.popleft()
            ans=max(ans,t)
            if i-1>=0 and not vis[i-1][j] and grid[i-1][j]==1:
                sources.append((i-1,j,t+1))
                vis[i-1][j]=True
            if i+1<n and not vis[i+1][j] and grid[i+1][j]==1:
                sources.append((i+1,j,t+1))
                vis[i+1][j]=True
            if j-1>=0 and not vis[i][j-1] and grid[i][j-1]==1:
                sources.append((i,j-1,t+1))
                vis[i][j-1]=True
            if j+1<m and not vis[i][j+1] and grid[i][j+1]==1:
                sources.append((i,j+1,t+1))
                vis[i][j+1]=True
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    return -1
        return ans

        


        