class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows = len(grid)

        columns = len(grid[0])

        for i in range(rows):
            for j in range(columns):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += (grid[i][j - 1])
                elif j == 0:
                    grid[i][j] += (grid[i - 1][j])
                else:
                    grid[i][j] += (min(grid[i - 1][j], grid[i][j - 1]))
        
        return grid[-1][-1]