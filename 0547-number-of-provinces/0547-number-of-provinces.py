
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n
                self.count = n  # Initially, each city is a province

            def find(self, x):
                # Find the root and shorten the path
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, a, b):
                root_a = self.find(a)
                root_b = self.find(b)

                # Already in the same group
                if root_a == root_b:
                    return False

                # Keep the taller tree as the parent
                if self.rank[root_a] < self.rank[root_b]:
                    root_a, root_b = root_b, root_a

                self.parent[root_b] = root_a

                if self.rank[root_a] == self.rank[root_b]:
                    self.rank[root_a] += 1

                self.count -= 1  # Two groups become one
                return True

        n = len(isConnected)
        dsu = DSU(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    dsu.union(i, j)

        return dsu.count

        