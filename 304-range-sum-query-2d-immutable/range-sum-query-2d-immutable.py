class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        self.matrix = matrix
        self.map = [[0 for i in range(COLS + 1)] for _ in range(ROWS + 1)]

        for i in range(0, ROWS):
            c_sum = 0
            for j in range(0, COLS):
                c_sum += self.matrix[i][j]
                self.map[i+1][j+1] = c_sum + self.map[i][j+1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        return self.map[row2][col2] - self.map[row2][col1 - 1] - self.map[row1 - 1][col2] + self.map[row1 - 1][col1 - 1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)