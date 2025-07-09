from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        columns = len(grid[0])

        minutes = 0
        queue = deque()
        s = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    s.add((i,j))

        while queue:
            i, j, minute = queue.popleft()

            minutes = max(minutes, minute)

            for row, col in directions:
                nr = i + row
                nc = j + col

                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] not in s:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc, minute + 1))
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    return -1
        
        return minutes





        