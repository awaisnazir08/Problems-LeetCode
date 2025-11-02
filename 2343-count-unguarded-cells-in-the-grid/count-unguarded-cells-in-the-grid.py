class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """

        grid = [[-1] * n for _ in range(m)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def mark(guard):
            i, j = guard

            for row, col in directions:
                r, c = row + i, col + j
                while 0 <= r < m and 0 <= c < n:
                    if grid[r][c] == 2 or grid[r][c] == 1:
                        break
                    elif grid[r][c] == -1:
                        grid[r][c] = 0
                    r, c = r + row, c + col
    
        for i, j in guards:
            grid[i][j] = 1
        
        for i, j in walls:
            grid[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    mark((i, j))
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    res += 1
        
        return res

        