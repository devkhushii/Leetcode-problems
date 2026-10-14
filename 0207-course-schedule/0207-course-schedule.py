class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visited=[False]*numCourses
        recStack=[False]*numCourses

        def dfs(node):
            visited[node]=True
            recStack[node]=True

            for i in range(len(prerequisites)):
                u=prerequisites[i][1]
                v=prerequisites[i][0]
                if u==node:
                    if not visited[v]:
                        if dfs(v):
                            return True
                    elif recStack[v]:
                        return True
            recStack[node]=False
            return False

        for i in range(numCourses):
            if not visited[i]:

                if dfs(i):
                    return False
        return True
        