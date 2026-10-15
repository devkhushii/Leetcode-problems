
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]],
                          src: int, dst: int, k: int) -> int:

        graph = [[] for _ in range(n)]

        for u, v, wt in flights:
            graph[u].append([v, wt])

        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        pq = [(0, src, 0)]  # cost, node, flights used

        while pq:
            cost, node, used = heapq.heappop(pq)

            if node == dst:
                return cost

            if cost > dist[node][used]:
                continue

            if used == k + 1:
                continue

            for nei, wt in graph[node]:
                new_cost = cost + wt

                if new_cost < dist[nei][used + 1]:
                    dist[nei][used + 1] = new_cost
                    heapq.heappush(
                        pq, (new_cost, nei, used + 1)
                    )

        return -1

