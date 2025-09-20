class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        low = 0

        n = len(matrix)
        m = len(matrix[0])

        high = (n*m - 1)

        while low <= high:
            mid = (low + high) // 2

            mr, mc = mid // m, mid % m

            if matrix[mr][mc] == target:
                return True
            elif matrix[mr][mc] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False