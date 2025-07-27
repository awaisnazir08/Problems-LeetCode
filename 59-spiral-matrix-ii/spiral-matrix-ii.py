class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1

        value = 1

        while left <= right:
            # fill every value in the top row
            for column in range(left, right + 1):
                matrix[top][column] = value
                value += 1
            top += 1

            # fill every value in the right row
            for row in range(top, bottom + 1):
                matrix[row][right] = value
                value += 1
            right -= 1

            # fill every value in the bottom row (reverse order)
            for column in range(right, left - 1, -1):
                matrix[bottom][column] = value
                value += 1
            bottom -= 1

            # fill every value in the left row (reverse order)
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = value
                value += 1
            left += 1
            
        return matrix


