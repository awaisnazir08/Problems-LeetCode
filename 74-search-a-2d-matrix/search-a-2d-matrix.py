class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            middle = (top + bottom) // 2

            if matrix[middle][0] < target and matrix[middle][-1] > target:
                break
            elif matrix[middle][0] == target or matrix[middle][-1] == target:
                return True
            elif matrix[middle][0] > target:
                bottom = middle - 1
            else:
                top = middle + 1
        
        row = (top + bottom) // 2

        start = 0
        end = len(matrix[0]) - 1 

        while start <= end:
            middle = (start + end) // 2

            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        
        return False