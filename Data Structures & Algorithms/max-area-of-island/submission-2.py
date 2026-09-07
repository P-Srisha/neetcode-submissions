class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = collections.deque()
            grid[r][c] = 0
            q.append((r, c))
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0):
                        continue
                    q.append((r, c))
                    grid[r][c] = 0
                    res += 1
            return res


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))

        return res