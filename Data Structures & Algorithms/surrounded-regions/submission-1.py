class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = collections.deque()
        regions = []
        visit = set()

        def bfs(r, c):
            q.append((r, c))
            visit.add((r, c))
            region = []
            region.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or board[r][c] == 'X':
                        continue
                    q.append((r, c))
                    visit.add((r, c))
                    region.append((r, c))

            return region

        def surroundRegions():
            for region in regions:
                surrounded = True
                for r, c in region:
                    if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                        surrounded = False

                if surrounded:
                    for r, c in region:
                        board[r][c] = 'X'

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visit:
                    regions.append(bfs(r, c))

        # print(regions)

        surroundRegions()