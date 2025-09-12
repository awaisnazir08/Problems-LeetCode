class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        rows = len(grid)
        cols = len(grid[0])

        def bfs(queue):
            visited = set()

            while queue:
                r, c, v = queue.pop(0)
                visited.add((r, c))

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:
                        if grid[row][col] == 0:
                            visited.add((row, col))
                            queue.append((row, col, v + 1))
                        elif grid[row][col] == 1:
                            return v

        def mark(i, j):
            visited = set()
            visited.add((i, j))
            grid[i][j] = 2

            queue = []
            queue.append((i, j))

            while queue:
                r, c = queue.pop(0)
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:
                        if grid[row][col] == 1:
                            grid[row][col] = 2
                            visited.add((row, col))
                            queue.append((row, col))

        found = False
        for i in range(rows):
            if found:
                break
            for j in range(cols):
                if grid[i][j] == 1:
                    mark(i, j)
                    found = True
                    break
    
        start_cells = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    start_cells.append((i, j, 0))
        return bfs(start_cells)