class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        minHeap = [[grid[0][0], 0, 0]]
        start = [0, 0]
        visit = set()

        while minHeap:
            w, r, c = heapq.heappop(minHeap)

            if r == rows - 1 and c == cols - 1:
                return w

            if (r, c) in visit:
                continue

            visit.add((r, c))

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visit:
                    continue
                newW = max(grid[row][col], w)
                # visit.add((row, col))
                heapq.heappush(minHeap, [newW, row, col])