
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        
        n=len(points)
        graph = [[] for _ in range(n)]
        for i in range(len(points)):
            min_dis=float('inf')
            xi=points[i][0]
            yi=points[i][1]
            for j in range(i+1,len(points)):
                xj=points[j][0]
                yj=points[j][1]
                dist = abs(xi - xj) + abs(yi - yj)
                graph[i].append((j,dist))
                graph[j].append((i,dist))

        visited = set([0])
        pq = [(w, 0, v) for v, w in graph[0]]
        heapq.heapify(pq)
        mst_weight = 0
        mst_edges = []

        while pq and len(visited) < n:
            w, u, v = heapq.heappop(pq)
            if v in visited:
                continue                    # would form a cycle within the tree
            visited.add(v)
            mst_weight += w
            mst_edges.append((u, v, w))
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, v, neighbor))

        return mst_weight