class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj=[[] for _ in range(numCourses)]
        visited=[False]*numCourses
        recstack=[False]*numCourses
        stack=[]

        for v,u in prerequisites:
            adj[u].append(v)
        
        def dfs(node):
            visited[node]=True
            recstack[node]=True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recstack[neighbor]:
                    return True
            
            recstack[node]=False
            stack.append(node)
            return False

        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return []
                    
        return stack[::-1]