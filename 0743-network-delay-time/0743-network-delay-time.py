class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dist = [float('inf')] * n
        source=k
        dist[source-1] = 0

        for _ in range(n - 1):                  # relax all edges V-1 times
            updated = False
            for u, v, w in times:
                if dist[u-1] != float('inf') and dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w
                    updated = True
            if not updated:                     # early exit optimization
                break


        if float('inf') in dist:
                return -1

        return max(dist)
            