
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        visited = [False] * numCourses
        recStack = [False] * numCourses

        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)

        def dfs(node):
            visited[node] = True
            recStack[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recStack[neighbor]:
                    return True

            recStack[node] = False
            return False

        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False

        return True
