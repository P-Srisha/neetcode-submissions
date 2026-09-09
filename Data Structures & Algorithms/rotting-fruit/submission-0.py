class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))

        time = 0

        def bfs():
            nonlocal time
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        r, c = row + dr, col + dc

                        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                            continue
                        
                        grid[r][c] = 2
                        q.append((r, c))
                time += 1

        bfs()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
                
        return max(0, time - 1)