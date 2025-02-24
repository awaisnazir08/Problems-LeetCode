class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        def isMagicSquare(x, y):
            # if x + 2 >= rows or y + 2 >=cols:
            #     return False
            
            distinct_numbers = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if (grid[i][j] > 9) or (grid[i][j] == 0):
                        return False
                    distinct_numbers.add(grid[i][j])
            if len(distinct_numbers) != 9:
                return False
            
            s = set()

            s.add((grid[x][y] + grid[x][y + 1] + grid[x][y + 2]))
            s.add((grid[x + 1][y] + grid[x + 1][y + 1] + grid[x + 1][y + 2]))
            s.add((grid[x + 2][y] + grid[x + 2][y + 1] + grid[x + 2][y + 2]))

            s.add((grid[x][y] + grid[x + 1][y] + grid[x + 2][y]))
            s.add((grid[x][y + 1] + grid[x + 1][y + 1] + grid[x + 2][y + 1]))
            s.add((grid[x][y + 2] + grid[x + 1][y + 2] + grid[x + 2][y + 2]))
            
            s.add((grid[x][y] + grid[x + 1][y + 1] + grid[x + 2][y + 2]))
            s.add((grid[x][y + 2] + grid[x + 1][y + 1] + grid[x + 2][y]))

            return len(s) == 1
        
        magicSquares = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagicSquare(i, j):
                    magicSquares += 1
        
        return magicSquares
            