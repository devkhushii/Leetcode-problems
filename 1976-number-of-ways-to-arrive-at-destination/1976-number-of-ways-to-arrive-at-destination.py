
import heapq

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]

        # Build the undirected weighted graph
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        dist = [float('inf')] * n  # Shortest time to each node
        ways = [0] * n              # Number of shortest paths to each node

        dist[0] = 0
        ways[0] = 1                 # One way to start at node 0
        heap = [(0, 0)]             # (time, node)

        while heap:
            time, node = heapq.heappop(heap)

            # Ignore an outdated heap entry
            if time > dist[node]:
                continue

            for neighbor, road_time in graph[node]:
                new_time = time + road_time

                if new_time < dist[neighbor]:
                    # Found a shorter route: replace old information
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(heap, (new_time, neighbor))

                elif new_time == dist[neighbor]:
                    # Found another route with the same shortest time
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]
