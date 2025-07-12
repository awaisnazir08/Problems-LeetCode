from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        # If starting or ending point is blocked
        if grid[0][0] != 0 or grid[rows - 1][columns - 1] != 0:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        visited = set()
        q = deque([(0, 0, 1)])  # row, col, path length
        visited.add((0, 0))

        while q:
            r, c, l = q.popleft()

            if r == rows - 1 and c == columns - 1:
                return l

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 0:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc, l + 1))

        return -1  # No path found
