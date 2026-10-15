class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])   # path compression
                return self.parent[x]

            def union(self, x, y):
                rx, ry = self.find(x), self.find(y)
                if rx == ry:
                    return False              # already connected -> would form a cycle
                if self.rank[rx] < self.rank[ry]:
                    rx, ry = ry, rx
                self.parent[ry] = rx
                if self.rank[rx] == self.rank[ry]:
                    self.rank[rx] += 1
                return True

        def kruskal_mst(n, edges):
            """
            edges: list of (weight, u, v)
            """
            edges = sorted(edges)             # sort ALL edges by weight ascending
            dsu = DSU(n)
            mst_weight = 0
            mst_edges = []

            for weight, u, v in edges:
                if dsu.union(u, v):           # only add if it doesn't form a cycle
                    mst_weight += weight
                    mst_edges.append((u, v, weight))
                    if len(mst_edges) == n - 1:
                        break                  # MST complete

            return mst_weight
        edges=[]
        n=len(points)
        for i in range(len(points)):
            min_dis=float('inf')
            xi=points[i][0]
            yi=points[i][1]
            for j in range(i+1,len(points)):
                xj=points[j][0]
                yj=points[j][1]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append((dist, i, j))
        
        return kruskal_mst(n, edges)
