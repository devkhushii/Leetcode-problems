
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(m):
            for c in range(n):

                # Start DFS for each unvisited land cell
                if grid[r][c] > 0:
                    stack = [(r, c)]
                    island_sum = 0

                    # Mark visited when pushing onto stack
                    island_sum += grid[r][c]
                    grid[r][c] = 0

                    while stack:
                        x, y = stack.pop()

                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy

                            if (0 <= nx < m and
                                0 <= ny < n and
                                grid[nx][ny] > 0):

                                island_sum += grid[nx][ny]
                                grid[nx][ny] = 0
                                stack.append((nx, ny))

                    # Check the total value of this island
                    if island_sum % k == 0:
                        count += 1

        return count
