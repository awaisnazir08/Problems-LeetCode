class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        unique_paths_dp = [[0] * (columns + 2) for _ in range(rows + 2)]
        
        unique_paths_dp[1][0] = 1

        for i in range(1, rows + 1):
            for j in range(1, columns + 1):
                if obstacleGrid[i - 1][j - 1] == 1:
                    continue
                
                unique_paths_dp[i][j] = unique_paths_dp[i - 1][j] + unique_paths_dp[i][j-1]
        
        return unique_paths_dp[rows][columns]


