
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        visited = [False] * n

        dist[0] = 0
        cost = 0

        for _ in range(n):
            node = -1

            # Pick the nearest unvisited point
            for i in range(n):
                if not visited[i] and (node == -1 or dist[i] < dist[node]):
                    node = i

            visited[node] = True
            cost += dist[node]

            # Update distances to unvisited points
            for i in range(n):
                if not visited[i]:
                    new_dist = (abs(points[node][0] - points[i][0])
                                + abs(points[node][1] - points[i][1]))
                    dist[i] = min(dist[i], new_dist)

        return cost
