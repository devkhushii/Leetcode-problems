class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        graph=[[] for _ in range(n)]

        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc=[-1]*n
        low=[0]*n
        time=[0]
        critical=[]

        def dfs(node,parent):
            disc[node]=low[node]=time[0]
            time[0]+=1

            for v in graph[node]:
                if v==parent:
                    continue
                if disc[v]==-1:
                    dfs(v,node)
                    low[node]=min(low[node],low[v])
                    if low[v]>disc[node]:
                        critical.append((node,v))
                else:
                    low[node]=min(low[node],disc[v])

        for node in range(n):
            if disc[node]==-1:
                dfs(node,-1)
        return critical


