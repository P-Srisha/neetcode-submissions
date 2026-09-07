class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        def bfs():
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 2147483647):
                        continue

                    grid[r][c] = grid[row][col] + 1
                    q.append((r, c))

        bfs()       