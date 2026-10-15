
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]],
                          src: int, dst: int, k: int) -> int:

        graph = [[] for _ in range(n)]

        for u, v, wt in flights:
            graph[u].append([v, wt])

        dist = [float('inf')] * n
        dist[src] = 0
        q = deque([(0, src,-1)])         
        
        while q:
            d, node,stop = q.popleft()   
        
            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor] and stop+1<=k:
                    dist[neighbor] = new_dist
                    q.append((new_dist,neighbor,stop+1))

        return dist[dst] if dist[dst]!=float('inf') else -1