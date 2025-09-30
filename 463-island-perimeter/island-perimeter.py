class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0

        rows = len(grid)
        cols = len(grid[0])

        def bfs(i, j):
            visited = set()

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            q = []
            parameter = 0

            q.append((i, j))
            visited.add((i, j))

            while q:
                row, col = q.pop(0)

                p = 4
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc]:
                            p -= 1
                            if (nr, nc) not in visited:
                                visited.add((nr, nc))
                                q.append((nr, nc))
                parameter += p
            return parameter
                    





        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return bfs(i, j)
        
        return 0